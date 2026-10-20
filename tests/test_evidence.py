"""Unit and break tests for the evidence ledger verifier (scripts/evidence.py).

Run: python3 -m unittest discover -s tests -v
The ledger tests need the pinned source cache (python3 scripts/download_sources.py); they are skipped otherwise.
"""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evidence  # noqa: E402

CACHE_READY = all(evidence.source_sha_ok(s) for s in ("arxiv_2302.13971", "arxiv_2206.14858", "arxiv_2401.04088"))


class NumberMatching(unittest.TestCase):
    CASES = [
        (5000, "5,000 test", True), (12032, "12,032 questions", True), (5000, "15,000", False),
        (68.5, "68.5%", True), (68.5, "68.50", True), (68.5, "168.5", False), (68.5, "68.55", False),
        (60.0, "60.0%", True), (60.0, "60%", True), (60.0, "60.1", False),
        (61, "at 61%", True), (61, "61.0%", True), (61, "61.5%", False),
        (72.31, "72.31%", True), (72.31, "72.3%", False), (0.078, "0.078", True), (93.3, "93.3,", True),
    ]

    def test_value_patterns(self):
        for value, text, expected in self.CASES:
            with self.subTest(value=value, text=text):
                self.assertEqual(bool(evidence.fmt_number_pattern(value).search(text)), expected)

    def test_cell_token_strips_marks(self):
        self.assertEqual(evidence.cell_token("gpt-4o chatgpt[^1] `88.7` `53.6`", 3), "53.6")
        self.assertEqual(evidence.cell_token("Model 74.9* 67.3%", 1), "74.9")
        self.assertEqual(evidence.cell_token("x 1,319", 1), "1319")


@unittest.skipUnless(CACHE_READY, "pinned source cache not available")
class LedgerBreakTests(unittest.TestCase):
    """Each mutation must make a passing claim fail. If a gate is disabled, its test fails."""

    @classmethod
    def setUpClass(cls):
        cls.claims = {c["id"]: c for c in evidence.load_claims()}
        cls.base = cls.claims["llama1.minerva-540b.gsm8k.greedy"]
        cls.table = cls.claims["mixtral-tr.mistral-7b.gsm8k"]

    def assert_fails(self, claim):
        self.assertTrue(evidence.check_claim(claim), f"mutation was not detected: {claim}")

    def test_whole_ledger_verifies(self):
        _, failures = evidence.verify_all(verbose=False)
        self.assertEqual(failures, {})

    def test_baseline_passes(self):
        self.assertEqual(evidence.check_claim(self.base), [])
        self.assertEqual(evidence.check_claim(self.table), [])

    def test_changed_value(self):
        c = copy.deepcopy(self.base)
        c["value"] = 68.6
        self.assert_fails(c)

    def test_changed_quote(self):
        c = copy.deepcopy(self.base)
        c["quotes"][0] = "540B 33.6 50.3 58.8 78.5"
        self.assert_fails(c)

    def test_wrong_page(self):
        c = copy.deepcopy(self.base)
        c["page"] = 7
        self.assert_fails(c)

    def test_wrong_source(self):
        c = copy.deepcopy(self.base)
        c["source"] = "arxiv_2206.14858"
        self.assert_fails(c)

    def test_wrong_column(self):
        # 50.0 is the GSM8K cell (token 14); binding it to the MATH column (token 13) must fail
        c = copy.deepcopy(self.table)
        c["token"] = 13
        self.assert_fails(c)

    def test_value_from_neighbouring_cell(self):
        # A value that occurs in the row but sits in another column (LLaMA 2 13B MBPP, not a GSM8K score)
        c = copy.deepcopy(self.claims["mixtral-tr.llama2-13b.mbpp"])
        c["token"] = 14
        self.assert_fails(c)

    def test_short_quote_rejected(self):
        c = copy.deepcopy(self.base)
        c["quotes"] = ["68.5"]
        self.assert_fails(c)

    def test_absent_text_present(self):
        c = copy.deepcopy(self.claims["helm-v030.humaneval.only-code-models"])
        c["absent"] = ["code-davinci-002"]
        self.assert_fails(c)

    def test_anchor_mismatch(self):
        c = copy.deepcopy(self.claims["aa.sonnet-55.terminal-bench-4"])
        c["anchor"] = {"pattern": c["anchor"]["pattern"], "expect": "\"name\":\"Claude Opus 5.5\""}
        self.assert_fails(c)

    def test_scaled_value_mismatch(self):
        c = copy.deepcopy(self.claims["aa.sonnet-55.terminal-bench-4"])
        c["value"] = 64.6
        self.assert_fails(c)

    def test_unknown_source(self):
        c = copy.deepcopy(self.base)
        c["source"] = "arxiv_9999.99999"
        self.assert_fails(c)


if __name__ == "__main__":
    unittest.main()
