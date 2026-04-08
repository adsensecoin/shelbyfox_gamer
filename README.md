# ⚡ OptiFlow Gamer OS

> **A sovereign, modular, AI-powered gaming operating system.**
> Not an emulator — an intelligence layer over simulated gaming worlds.

[![CI](https://github.com/shelbyfox/optiflow-gamer-os/actions/workflows/ci.yml/badge.svg)](https://github.com/shelbyfox/optiflow-gamer-os/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Core: Sealed](https://img.shields.io/badge/Core-Sealed%20%F0%9F%94%92-red)](MANIFEST.md)

---

## What is OptiFlow Gamer OS?

OptiFlow is not just an emulator wrapper. It is a **runtime orchestration platform** that:

- 🔌 Loads emulators as **hot-swappable plugins** (mGBA, PPSSPP, Dolphin, NeoGeo)
- 🤖 Applies a **reinforcement learning AI** that watches and plays games autonomously
- ⚡ Dynamically **optimizes performance** via the Turbo subsystem (FPS, CPU, GPU)
- 🔒 Protects a **sovereign, immutable core** while enabling a fully open ecosystem
- 🌐 Exposes everything through a **gRPC + WebSocket orchestrator** for real-time control

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  OPTIFLOW GAMER OS                  │
│  ┌──────────┐  ┌────────────┐  ┌──────────────────┐ │
│  │  CORE    │  │  PLUGINS   │  │    AI ENGINE     │ │
│  │ (sealed) │  │ (emulators)│  │ (RL + Vision)    │ │
│  └────┬─────┘  └─────┬──────┘  └────────┬─────────┘ │
│       │              │                  │            │
│  ┌────▼──────────────▼──────────────────▼──────────┐ │
│  │           ORCHESTRATOR (gRPC + WS)              │ │
│  └─────────────────────────────────────────────────┘ │
│  ┌──────────────────┐  ┌──────────────────────────┐  │
│  │  TURBO ENGINE    │  │  CLI / Dashboard         │  │
│  └──────────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## Quick Start

### Prerequisites
- Node.js 20 LTS
- Python 3.11+
- Docker + Docker Compose
- Redis 7 (or use Docker)

### 1. Clone & Install

```bash
git clone https://github.com/shelbyfox/optiflow-gamer-os.git
cd optiflow-gamer-os
npm install
```

### 2. Setup Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start Full Stack (Docker)

```bash
docker-compose up --build
```

### 4. Launch a Game via CLI

```bash
# Install CLI globally
npm run build:cli
npm install -g ./cli

# Start a ROM with AI enabled
optiflow start ./roms/pokemon.gba --plugin mgba --ai
```

---

## Project Structure

```
optiflow-gamer-os/
├── core/           🔒 Sealed kernel (owner-only)
├── sdk/            📦 Public developer contracts
├── plugins/        🔌 Community emulator plugins
├── ai/             🤖 Python AI microservice
├── turbo/          ⚡ Performance optimization engine
├── orchestrator/   🧠 Central API + WebSocket server
├── cli/            💻 Terminal interface
└── docs/           📚 Documentation
```

---

## Contributing

The **ecosystem is open**. The **core is sealed**.

| Area          | Open to Community? |
|---------------|-------------------|
| `plugins/`    | ✅ Yes             |
| `ai/reward-system/` | ✅ Yes      |
| `docs/`       | ✅ Yes             |
| `core/`       | ❌ Owner-only      |
| `sdk/`        | ❌ Owner-only      |

See [CONTRIBUTING.md](CONTRIBUTING.md) and [MANIFEST.md](MANIFEST.md) for details.

---

## License

MIT — free to use, extend, and distribute.
Core modules are additionally protected by cryptographic signing.
See [SECURITY.md](SECURITY.md) for details.

---

*Built with 🔥 by shelbyfox | Powered by TypeScript + Python + PyTorch*
