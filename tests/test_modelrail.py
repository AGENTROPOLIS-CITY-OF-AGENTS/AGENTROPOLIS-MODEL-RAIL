import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from modelrail.policy import PolicyDenied, RequestPolicy
from modelrail.providers import run_agy, ProviderError
from modelrail.receipts import write_receipt, verify_receipts

class PolicyTests(unittest.TestCase):
    def test_personal_agy_requires_optin(self):
        with self.assertRaises(PolicyDenied):
            RequestPolicy("agy", "personal", allow_cloud=True).check()
        RequestPolicy("agy", "personal", allow_cloud=True, personal_ack=True).check()

    def test_fleet_agy_blocked(self):
        with self.assertRaises(PolicyDenied):
            RequestPolicy("agy", "fleet", allow_cloud=True, personal_ack=True).check()

    def test_unknown_provider_blocked(self):
        with self.assertRaises(PolicyDenied):
            RequestPolicy("mystery", "personal").check()

    def test_cloud_opt_in(self):
        with self.assertRaises(PolicyDenied):
            RequestPolicy("gemini-api", "fleet").check()
        RequestPolicy("gemini-api", "fleet", allow_cloud=True).check()
        RequestPolicy("ollama", "fleet").check()

class ReceiptTests(unittest.TestCase):
    def test_chain_and_tamper(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "receipts.jsonl"
            for prompt in ("a", "b"):
                write_receipt(path, provider="ollama", purpose="personal", model="test",
                              prompt=prompt, response="ok", status="success", duration_ms=3)
            self.assertEqual(verify_receipts(path), (True, 2))
            content = path.read_text().replace('"duration_ms":3', '"duration_ms":4', 1)
            path.write_text(content)
            self.assertEqual(verify_receipts(path), (False, 0))

class AgyTests(unittest.TestCase):
    @patch("modelrail.providers.shutil.which", return_value="/usr/bin/agy")
    @patch("modelrail.providers.subprocess.run")
    def test_stdin_prompt_and_sandbox(self, runner, which):
        from types import SimpleNamespace
        runner.return_value = SimpleNamespace(returncode=0, stdout=json.dumps({
            "event": "result", "result": {"status": "SUCCESS", "response": "OK", "usage": {}}
        }), stderr="")
        answer, meta = run_agy("Secret prompt", "example-model", 10)
        self.assertEqual(answer, "OK")
        args = runner.call_args.args[0]
        self.assertIn("--sandbox", args)
        self.assertNotIn("Secret prompt", args)
        payload = json.loads(runner.call_args.kwargs["input"])
        self.assertEqual(payload["message"]["content"], "Secret prompt")

    @patch("modelrail.providers.shutil.which", return_value=None)
    def test_missing_cli(self, which):
        with self.assertRaises(ProviderError):
            run_agy("test", None, 10)

if __name__ == "__main__":
    unittest.main()
