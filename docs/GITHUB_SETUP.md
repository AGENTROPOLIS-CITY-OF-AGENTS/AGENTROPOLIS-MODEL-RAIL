# New GitHub repository setup

Recommended owner: AGENTROPOLIS-CITY-OF-AGENTS
Repository name: AGENTROPOLIS-MODELRAIL
Description: Local-first AI model routing utility with policy-gated providers, Hermes integration, ATG execution envelopes, and auditable inference receipts.
License: MIT (already included as LICENSE)
Visibility: Public (if the maintainer approves open release)
Topics: agentropolis, hermes-agent, model-router, agentic-ai, local-first, ai-governance, ollama, python

## Avoid duplicate files

Create the repository empty: do NOT initialize with a GitHub README,
.gitignore, or license. The package already includes those files.
The correct GitHub license selector value would be MIT; uploading the
included LICENSE automatically makes GitHub recognize that license.

## Upload as source

Do not upload the ZIP as your only repository file. Extract this package
so README.md, LICENSE, modelrail/, tests/, etc. live in the repository root.
The ZIP itself can be attached as a GitHub release artifact after testing.

## CLI workflow (after new repo exists)

    git clone https://github.com/AGENTROPOLIS-CITY-OF-AGENTS/AGENTROPOLIS-MODELRAIL.git
    cd AGENTROPOLIS-MODELRAIL
    # Copy the extracted contents of this package here, including .github and .gitignore
    python3 -m unittest discover -s tests -v
    git add .
    git commit -m "chore: bootstrap MODELRAIL alpha with policy guards and CI"
    git push -u origin main

Confirm the account has write access. Prefer a feature branch plus PR if main is protected.
GitHub Actions CI runs only offline tests and does not require cloud secrets.

## Next gates

1. Enable branch protection + require CI and reviewed PRs.
2. Enable secret scanning / push protection (if available).
3. Enable private vulnerability reports.
4. Assign AEGIS and VERITY independent audit owners.
5. Only tag an alpha after CI and verification receipts.