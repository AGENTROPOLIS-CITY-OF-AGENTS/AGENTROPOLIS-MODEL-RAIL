# AGENTROPOLIS MODELRAIL v0.1.0-alpha (repo-ready prototype)

A **local-first, read-only prototype** of a governed model utility. This is an original starter inspired by [neerazz/hermes-antigravity-oauth](https://github.com/neerazz/hermes-antigravity-oauth) (MIT), **not** an already-installed Hermes replacement or a live OAuth fork.

## Repository status

This repository is an independently versioned AGENTROPOLIS infrastructure utility. The Hermes plugin belongs in `integrations/hermes/` as a future adapter, not as the owner of this code. There is **no installable Hermes plugin** in this alpha release. See [`docs/GITHUB_SETUP.md`](docs/GITHUB_SETUP.md), [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and [`integrations/hermes/README.md`](integrations/hermes/README.md).

## Architecture

`Identity -> Mandate -> Provider Policy -> Model Adapter -> Receipt -> Audit`

Available modes:

| Provider | Backend | Usage | Restriction |
| --- | --- | --- | --- |
| `ollama` | Loopback `127.0.0.1:11434` | Personal/fleet | Requires local running Ollama + installed model |
| `agy` | Official, unmodified Google Antigravity CLI via JSON stdio | Personal only | Own sign-in, low concurrency, no credential access, never shared |
| `gemini-api` | Google public Generative Language REST API | Authorized API | Requires `GEMINI_API_KEY` and explicit cloud opt-in |

`agy` requires a **single user's** own local login, per Google's October 2026 forum clarification; never republish Antigravity OAuth credentials or run a shared subscription relay. Google's published Terms remain broader, so revalidate legal/policy guidance before release. API lane exists for actual fleet workloads.

## Install (Python 3.10+)

```sh
python3 -m pip install -e .
modelrail doctor
```

Use a Python virtual environment if system Python disallows user installs.

## Examples

Local-first (Ollama model already installed):

```sh
printf 'Summarize the execution-envelope concept.' | modelrail run --provider ollama --model YOUR_LOCAL_MODEL
```

Single-user Google Antigravity CLI (requires official `agy` sign-in performed by the user):

```sh
printf 'Explain ATG in one paragraph.' | modelrail run --provider agy --purpose personal --personal-ack --allow-cloud --model YOUR_AGY_MODEL
```

Fleet-eligible Gemini API (not personal Antigravity subscription):

```sh
export GEMINI_API_KEY='...set securely in your local shell or secret manager...'
printf 'List API design risks.' | modelrail run --provider gemini-api --purpose fleet --allow-cloud --model YOUR_APPROVED_GEMINI_MODEL
```

Receipts contain **hashes only**, not prompts or responses:

```sh
modelrail verify
```

## What is implemented

- Read-only CLI question -> response flow; local model + personal official CLI + authorized API lane.
- Provider policy: unknown providers denied, personal CLI never permitted for fleet, cloud use explicit.
- `agy` stdin JSON event transport avoids prompt exposure in process-argument lists, requests `--sandbox`, runs with a temporary empty working directory. It does **not** read or link Google credentials.
- Hash-chain JSONL local receipts with SHA-256 hashes of input/output, timestamps, provider/mode, elapsed duration.
- Fail-closed error paths and basic unit tests.

## NOT production ready

- **No live provider call has been tested** here; test suite uses mocks for `agy` and offline checks.
- This starter is **not** a full Hermes provider plugin or fork of the upstream source; adding native Hermes hooks is a separate phase.
- **No AEGIS service integration, signed receipts, off-host anchoring, ATG compiler, multi-writer lock, credential vault, token-cost dashboard or model-level permission gate** is implemented.
- Local JSONL hash-chains are **not tamper-evident against a host administrator**; anchor signed receipts off-host for production.
- `agy` sandbox is not a security boundary equivalent to VM/container isolation, and the official CLI controls its own tools and workspace permissions. Evaluate headless permission settings and isolate the account/machine prior to using untrusted prompts.
- Ollama API bound to loopback; local server misconfiguration could still increase exposure.
- Rate limits, retries, concurrency caps and model validation have not been integrated.

## Verification

```sh
python3 -m unittest discover -s tests -v
```

## Source credit

Architecture studied: Neeraj Kumar Singh Beshane, [hermes-antigravity-oauth](https://github.com/neerazz/hermes-antigravity-oauth), MIT. This starter is newly authored and does not vendor his source. If you fork and incorporate upstream source, preserve its original MIT copyright/license notice and history.

## Production split

- Personal `agy` subprocess usage is only for one human's interactive or low-volume personal tasks.
- Hermes shared fleet must use licensed API products or local models; it **must not** proxy an individual's subscription login.
- Promote only through a reviewed PR with security tests and independently verified runtime receipts.