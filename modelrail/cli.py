import argparse
import shutil
import sys
import time
from pathlib import Path

from modelrail.policy import RequestPolicy, PolicyDenied
from modelrail.providers import dispatch, ProviderError
from modelrail.receipts import default_receipt_path, write_receipt, verify_receipts

def make_parser():
    parser = argparse.ArgumentParser(prog="modelrail", description="Governed local-first model utility")
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("doctor", help="Check local adapter availability (no credentials inspected)")
    run = subs.add_parser("run", help="Run one read-only model question")
    run.add_argument("--provider", required=True, choices=["agy", "ollama", "gemini-api"])
    run.add_argument("--purpose", choices=["personal", "fleet"], default="personal")
    run.add_argument("--model")
    run.add_argument("--allow-cloud", action="store_true")
    run.add_argument("--personal-ack", action="store_true")
    run.add_argument("--prompt-file", type=Path)
    run.add_argument("--timeout", type=int, default=120)
    run.add_argument("--receipts", type=Path, default=default_receipt_path())
    check = subs.add_parser("verify", help="Verify local receipt hash chain")
    check.add_argument("--receipts", type=Path, default=default_receipt_path())
    return parser

def main(argv=None) -> int:
    args = make_parser().parse_args(argv)
    if args.command == "doctor":
        print("Official agy:", "found" if shutil.which("agy") else "not found")
        print("Ollama:", "found" if shutil.which("ollama") else "not found")
        print("Gemini API: adapter available; credentials NOT inspected")
        print("MODE: local-first, AGY strictly personal, cloud use opt-in")
        return 0
    if args.command == "verify":
        if not args.receipts.exists():
            print("No receipt file", file=sys.stderr)
            return 1
        try:
            valid, count = verify_receipts(args.receipts)
        except (OSError, ValueError, KeyError):
            valid, count = False, 0
        print(f"{'VALID' if valid else 'INVALID'}: {count} local receipt(s)")
        return 0 if valid else 1
    try:
        RequestPolicy(args.provider, args.purpose, args.allow_cloud, args.personal_ack).check()
        if args.timeout < 1 or args.timeout > 1800:
            raise PolicyDenied("Timeout must be between 1 and 1800 seconds")
        if args.prompt_file:
            prompt = args.prompt_file.read_text(encoding="utf-8")
        else:
            if sys.stdin.isatty():
                raise PolicyDenied("Pipe input over stdin or supply --prompt-file")
            prompt = sys.stdin.read(64_001)
        if not prompt.strip() or len(prompt) > 64_000:
            raise PolicyDenied("Prompt must be nonempty and at most 64,000 characters")
        start = time.monotonic()
        response, _metadata = dispatch(args.provider, prompt, args.model, args.timeout)
        elapsed = round((time.monotonic() - start) * 1000)
        receipt = write_receipt(args.receipts, provider=args.provider, purpose=args.purpose,
                                model=args.model, prompt=prompt, response=response,
                                status="success", duration_ms=elapsed)
        print(response)
        print(f"[MODELRAIL receipt {receipt['receipt_hash'][:12]} | local-only chain]", file=sys.stderr)
        return 0
    except (PolicyDenied, ProviderError, OSError, ValueError) as exc:
        print(f"DENIED / FAILED: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
