"""Adapters. Never access, copy, inspect, or relay provider OAuth credentials."""
import json
import os
import shutil
import subprocess
import tempfile
import urllib.error
import urllib.request

class ProviderError(RuntimeError):
    pass

def run_agy(prompt: str, model: str | None, timeout: int) -> tuple[str, dict]:
    """Invoke official unmodified agy CLI for a single local personal user only."""
    binary = shutil.which("agy")
    if not binary:
        raise ProviderError("Official agy CLI is not installed or on PATH")
    args = [binary, "--input-format", "stream-json", "--output-format", "stream-json", "--sandbox"]
    if model:
        args.extend(["--model", model])
    payload = json.dumps({"event": "user", "message": {"content": prompt}}, ensure_ascii=False) + "\n"
    with tempfile.TemporaryDirectory(prefix="modelrail_agy_") as wd:
        try:
            proc = subprocess.run(args, input=payload, text=True, capture_output=True,
                                  cwd=wd, timeout=timeout, check=False)
        except subprocess.TimeoutExpired as exc:
            raise ProviderError("Antigravity CLI timed out") from exc
    if proc.returncode:
        raise ProviderError(f"Antigravity CLI failed with exit code {proc.returncode}; inspect local CLI setup")
    results = []
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("event") == "result" and isinstance(event.get("result"), dict):
            results.append(event["result"])
    if not results:
        raise ProviderError("Antigravity CLI produced no result event")
    last = results[-1]
    if last.get("status") != "SUCCESS":
        raise ProviderError("Antigravity CLI returned a non-success result")
    return str(last.get("response") or ""), {"usage": last.get("usage", {})}

def run_ollama(prompt: str, model: str, timeout: int) -> tuple[str, dict]:
    url = "http://127.0.0.1:11434/api/generate"
    body = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read(8_000_000).decode())
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        raise ProviderError("Local Ollama request failed") from exc
    if not isinstance(data.get("response"), str):
        raise ProviderError("Invalid Ollama response")
    return data["response"], {"usage": {"input_tokens": data.get("prompt_eval_count"), "output_tokens": data.get("eval_count")}}

def run_gemini_api(prompt: str, model: str, timeout: int) -> tuple[str, dict]:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ProviderError("GEMINI_API_KEY missing from environment")
    if not model or not all(c.isalnum() or c in "-_." for c in model):
        raise ProviderError("Invalid Gemini model identifier")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json", "x-goog-api-key": key})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read(8_000_000).decode())
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        raise ProviderError("Gemini API request failed (verify credentials, quota and network)") from exc
    try:
        parts = data["candidates"][0]["content"]["parts"]
        response = "\n".join(p.get("text", "") for p in parts if isinstance(p, dict))
    except (IndexError, KeyError, TypeError) as exc:
        raise ProviderError("Gemini API response contains no usable candidate") from exc
    return response, {"usage": data.get("usageMetadata", {})}

def dispatch(provider: str, prompt: str, model: str | None, timeout: int) -> tuple[str, dict]:
    if provider == "agy":
        return run_agy(prompt, model, timeout)
    if not model:
        raise ProviderError("--model is required for this provider")
    if provider == "ollama":
        return run_ollama(prompt, model, timeout)
    if provider == "gemini-api":
        return run_gemini_api(prompt, model, timeout)
    raise ProviderError("Provider not available")
