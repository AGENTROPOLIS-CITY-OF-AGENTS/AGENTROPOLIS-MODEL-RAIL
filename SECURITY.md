# Security Policy

Status: alpha research utility, not approved for production agent execution.

## Report vulnerabilities

Use GitHub's private vulnerability reporting feature on this repository if enabled.
Do not publish active credentials, exploit logs, private prompts, or sensitive inference results in an issue. If private reporting is not yet configured, contact the repository maintainers through an approved private channel.

## Trust boundaries

- No consumer-subscription OAuth relay, token extraction, token symlinking, or credential sharing.
- The `agy` adapter invokes the official CLI for a single local personal user only; the account owner must follow current provider terms.
- Fleet use must rely on approved API contracts, enterprise endpoints, or local inference.
- `--allow-cloud` is required for network inference; never send confidential work without documented permission.
- Hash-only receipts are local integrity checks, not protected off-host records; they can be replaced by a host administrator.
- Running `agy --sandbox` does not establish an independent isolation boundary. Use a dedicated low-trust environment and explicit user approvals.
- Input and output contents can still be visible to invoked model providers and local processes; hash-only receipts do not guarantee prompt confidentiality.
- Never disable Hermes native tool approvals to connect the adapter.

## No credentials in CI

CI intentionally uses mocked/offline tests only. Never add long-lived inference credentials to pull-request workflows.

## Release blockers

No production release without security review, live provider contract tests, dependency scanning, process lifecycle verification, signed/off-host receipts, provider-specific rate controls, and documented data handling.