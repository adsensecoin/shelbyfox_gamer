# Security Policy — OptiFlow Gamer OS

## Reporting a Vulnerability

**Do NOT open a public GitHub issue for security vulnerabilities.**

Report vulnerabilities privately via:
- GitHub Security Advisory (preferred): Settings → Security → Advisories → New Draft
- Email: security@optiflow.dev (placeholder — update with real address)

We will acknowledge within **48 hours** and provide a fix timeline within **7 days**.

## Core Immutability

The `core/` and `sdk/` directories are cryptographically protected:
- Every release artifact is signed with an Ed25519 key held exclusively by the project owner.
- The public key is embedded in the runtime and verified at boot.
- Any modification to core modules without a matching signature will cause a boot failure.

## Plugin Security

All plugins distributed through the official OptiFlow registry must:
1. Pass automated security scanning (Semgrep + OSV)
2. Be signed by the OptiFlow owner key
3. Declare all required permissions in `plugin.manifest.json`

Community plugins that are **not** in the official registry are **unsigned** and will not load by default.
Users may explicitly enable unsigned plugins at their own risk via `OPTIFLOW_ALLOW_UNSIGNED=true`.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | ✅ Yes     |
| < 1.0   | ❌ No      |
