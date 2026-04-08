# Contributing to OptiFlow Gamer OS

Thank you for your interest in contributing! Before you start, please read this guide carefully.

---

## The Golden Rule

> **The ecosystem is open. The core is sealed.**

| Area                  | Community can... |
|-----------------------|-----------------|
| `plugins/`            | Add new emulator plugins |
| `ai/reward-system/`   | Add new reward functions for new games |
| `docs/`               | Improve documentation |
| `examples/`           | Add usage examples |
| **`core/`**           | ❌ **Off-limits** — owner-only |
| **`sdk/`**            | ❌ **Off-limits** — owner-only |

---

## How to Contribute a Plugin

### Step 1 — Fork & Clone

```bash
git clone https://github.com/shelbyfox/optiflow-gamer-os.git
cd optiflow-gamer-os
npm install
```

### Step 2 — Scaffold Your Plugin

```bash
mkdir plugins/my-emulator
cd plugins/my-emulator
```

Create `plugin.manifest.json` and `index.ts` following the [Plugin Development Guide](docs/plugin-dev-guide.md).

### Step 3 — Test Locally

```bash
# Enable unsigned mode for development
cp .env.example .env
# Set OPTIFLOW_ALLOW_UNSIGNED=true in .env

npm run build
optiflow plugins list
```

### Step 4 — Submit a PR

1. Push your branch to your fork
2. Open a PR against `main`
3. Fill out the PR template completely
4. Request plugin signing from @shelbyfox in the PR comments

> **Note**: Your plugin will not be included in official releases until signed by the owner.

---

## How to Contribute a Reward Function

For a new game AI agent, add a reward function in `ai/reward-system/`:

```python
# ai/reward-system/my_game_reward.py
from dataclasses import dataclass

@dataclass
class MyGameState:
    # Game-specific state fields
    score: int = 0

class MyGameRewardSystem:
    def compute(self, state: MyGameState) -> float:
        # Return a float reward signal
        return float(state.score) / 1000.0

    def reset(self) -> None:
        pass
```

Then submit a PR — no signing required for reward functions.

---

## Code Standards

### TypeScript
- All code must pass `npm run build` (TypeScript strict mode)
- Follow existing naming conventions
- No `any` types without explicit `// eslint-disable` comment with reason

### Python
- Python 3.11+ type hints required
- Must pass `mypy --strict`
- Use `dataclasses` for state objects

---

## Commit Convention

We use Conventional Commits:

```
feat: add PPSSPP emulator plugin
fix: correct frame buffer alignment in mGBA plugin
docs: add reward function guide for NeoGeo
test: add unit tests for FPSGovernor
```

---

## Code of Conduct

Be respectful. Focus on the technical merit of contributions.
Discrimination, harassment, or toxicity will result in an immediate ban.

---

## Questions?

Open a [GitHub Discussion](https://github.com/shelbyfox/optiflow-gamer-os/discussions) — not an Issue.
Issues are for bugs and confirmed feature requests only.
