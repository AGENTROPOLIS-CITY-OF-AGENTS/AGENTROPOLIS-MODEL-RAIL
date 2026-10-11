# Contributing to AGENTROPOLIS MODELRAIL

This is an infrastructure project with default-deny provider permissions and a documented personal/fleet split.

1. Open an issue describing the adapter or policy change and its trust boundary.
2. Work on a feature branch and submit a pull request, not a direct push to protected main.
3. Add offline tests and document which features are mocked or unverified.
4. Do not commit account credentials, private prompts, token cache copies, or unreviewed provider access paths.
5. Preserve upstream third-party licenses/attributions if importing code.
6. Changes enabling tools, network egress, multi-user access, or receipt signing require independent security review and human approval.

Do not represent a proposed Hermes plugin as installable until the Hermes compatibility suite has run successfully.