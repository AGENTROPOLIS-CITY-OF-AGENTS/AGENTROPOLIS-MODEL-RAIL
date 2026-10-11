"""Local JSONL hash-chain receipts. Not externally anchored or tamper-proof."""
import datetime
import hashlib
import json
import os
from pathlib import Path

def digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def canonical(value: dict) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def default_receipt_path() -> Path:
    return Path.home() / ".local" / "share" / "agentropolis-modelrail" / "receipts.jsonl"

def write_receipt(path: Path, *, provider: str, purpose: str, model: str | None,
                  prompt: str, response: str, status: str, duration_ms: int) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = "0" * 64
    if path.exists():
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if lines:
            previous = json.loads(lines[-1])["receipt_hash"]
    record = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "provider": provider, "purpose": purpose, "model": model,
        "prompt_sha256": digest(prompt), "response_sha256": digest(response),
        "status": status, "duration_ms": duration_ms, "prev_hash": previous,
    }
    record["receipt_hash"] = digest(canonical(record))
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(fd, "a", encoding="utf-8") as output:
        output.write(canonical(record) + "\n")
    return record

def verify_receipts(path: Path) -> tuple[bool, int]:
    previous = "0" * 64
    count = 0
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            item = json.loads(line)
            own_hash = item.pop("receipt_hash")
            if item.get("prev_hash") != previous or digest(canonical(item)) != own_hash:
                return False, count
            previous = own_hash
            count += 1
    return True, count
