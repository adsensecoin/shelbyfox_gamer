# Changelog — OptiFlow Gamer OS

All notable changes to this project will be documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

---

## [Unreleased]

### Planned for v0.2.0
- PPSSPP plugin (PSP emulator)
- AI checkpoint loading via CLI
- Web dashboard (React) for real-time monitoring
- PostgreSQL session persistence
- GPU acceleration for PyTorch (CUDA / MPS)
- Save-state support in mGBA plugin
- NeoGeo plugin (fighting games)

---

## [0.1.0] — 2026-04-07

### Added
- **Sovereign Core** (`core/`) — sealed, cryptographically protected
  - TypeScript interfaces: `IPlugin`, `IEmulatorPlugin`, `IAIAgent`, `IOptimizer`
  - Typed EventBus (pub/sub, zero direct module coupling)
  - Plugin Loader with Ed25519 signature verification
  - System Bootstrap with graceful shutdown
- **Public SDK** (`sdk/`) — community plugin surface
  - `BaseEmulatorPlugin` abstract class
  - `AIHookBridge` gRPC client with fallback to manual mode
- **mGBA Plugin** (`plugins/mgba/`) — GBA/GB/GBC emulator
  - Child process wrapper + FFmpeg frame capture
  - Full `IEmulatorPlugin` implementation
- **AI Microservice** (`ai/`) — Python 3.11 + PyTorch
  - gRPC server (`optiflow.proto`)
  - OpenCV frame preprocessor (84×84 grayscale, 4-frame stack)
  - PPO agent (CNN Actor-Critic, ~3.2M parameters)
  - Pokémon GBA reward system (exploration + badges + battles)
  - 17-test suite (reward system + preprocessor)
- **Turbo Engine** (`turbo/`) — intelligent performance optimization
  - `ResourceMonitor` (CPU/RAM/GPU polling via `systeminformation`)
  - `FPSGovernor` (profile-based action decisions)
  - 3 profiles: `battery`, `balanced`, `turbo`
- **Orchestrator** (`orchestrator/`) — central control plane
  - Express REST API (health, plugins, game/start, turbo, AI)
  - WebSocket server (real-time metrics + AI decisions)
  - Redis state manager (game sessions, TTL-based expiry)
  - Multi-stage Docker build
- **CLI** (`cli/`) — terminal interface
  - `optiflow start <rom>` — launch game with AI
  - `optiflow plugins list` — list plugins
  - `optiflow turbo <profile>` — switch Turbo profile
  - `optiflow ai status` — AI service health
  - `optiflow sign <dir>` — sign a plugin (owner only)
  - `optiflow status` — full system health
- **GitHub Infrastructure**
  - `CODEOWNERS` — core sealed to owner @shelbyfox
  - `ci.yml` — TypeScript build + Python mypy + pytest on every PR
  - `sign-core.yml` — Ed25519 plugin signing + release on tag push
  - `PULL_REQUEST_TEMPLATE.md`
- **Docs**
  - `MANIFEST.md` — project philosophy and standards
  - `docs/architecture.md` — system diagrams and data flows
  - `docs/plugin-dev-guide.md` — community plugin guide
  - `docs/ai-api.md` — gRPC API + agent architecture
  - `docs/turbo-api.md` — profiles + optimization actions
- **DevOps**
  - `docker-compose.yml` — Redis + PostgreSQL + AI + Orchestrator
  - `setup.py` — interactive environment setup script
  - `CONTRIBUTING.md`, `LICENSE`, `SECURITY.md`

---

*OptiFlow Gamer OS is built by shelbyfox — Sovereign AI Gaming Platform.*
