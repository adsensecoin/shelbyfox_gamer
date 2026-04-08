#!/usr/bin/env python3
"""
OptiFlow Gamer OS — Setup Script
Verifies environment, installs dependencies, generates proto stubs.
Run: python setup.py
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path


def print_header():
    print("\n" + "="*60)
    print("  ⚡ OptiFlow Gamer OS — Environment Setup")
    print("="*60 + "\n")


def check(label: str, ok: bool, fix: str = ""):
    status = "✅" if ok else "❌"
    print(f"  {status}  {label}")
    if not ok and fix:
        print(f"       → {fix}")
    return ok


def run(cmd: list[str], cwd: str | None = None) -> tuple[int, str]:
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout + result.stderr


def main():
    print_header()
    all_ok = True

    # ── Python ────────────────────────────────────────────────────────────
    print("Python:")
    py_version = sys.version_info
    ok = py_version >= (3, 11)
    all_ok &= check(
        f"Python {py_version.major}.{py_version.minor}.{py_version.micro}",
        ok,
        "Requires Python 3.11+. Download from https://python.org"
    )

    # ── Node.js ───────────────────────────────────────────────────────────
    print("\nNode.js:")
    code, out = run(["node", "--version"])
    node_ok = code == 0
    if node_ok:
        ver = out.strip().lstrip("v").split(".")
        node_ok = int(ver[0]) >= 20
    all_ok &= check(
        out.strip() if code == 0 else "Not found",
        node_ok,
        "Requires Node.js v20+. Download from https://nodejs.org"
    )

    code, out = run(["npm", "--version"])
    all_ok &= check(
        f"npm {out.strip()}" if code == 0 else "npm not found",
        code == 0,
        "npm should come with Node.js"
    )

    # ── Docker ────────────────────────────────────────────────────────────
    print("\nDocker:")
    code, out = run(["docker", "--version"])
    docker_ok = code == 0
    check(
        out.strip() if docker_ok else "Docker not found",
        docker_ok,
        "Optional for full stack. Download from https://docker.com"
    )

    code, out = run(["docker", "compose", "version"])
    check(
        out.strip().split("\n")[0] if code == 0 else "Docker Compose not found",
        code == 0,
        "Optional for full stack"
    )

    # ── mGBA ──────────────────────────────────────────────────────────────
    print("\nEmulator Dependencies:")
    mgba_path = shutil.which("mgba-sdl") or shutil.which("mgba")
    check(
        f"mGBA: {mgba_path}" if mgba_path else "mGBA not found",
        mgba_path is not None,
        "Install mGBA from https://mgba.io/downloads.html and add to PATH"
    )

    ffmpeg_path = shutil.which("ffmpeg")
    check(
        f"FFmpeg: {ffmpeg_path}" if ffmpeg_path else "FFmpeg not found",
        ffmpeg_path is not None,
        "Install FFmpeg from https://ffmpeg.org/download.html and add to PATH"
    )

    # ── Python packages ───────────────────────────────────────────────────
    print("\nPython Packages:")
    packages = ["numpy", "cv2", "torch", "grpc", "redis"]
    pkg_names = {"cv2": "opencv-python-headless", "grpc": "grpcio"}
    for pkg in packages:
        try:
            __import__(pkg)
            check(f"{pkg}", True)
        except ImportError:
            pip_name = pkg_names.get(pkg, pkg)
            check(f"{pkg}", False, f"pip install {pip_name}")

    # ── Install ───────────────────────────────────────────────────────────
    print("\nInstalling:")

    # Python deps
    print("  Installing Python requirements...")
    code, out = run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"], cwd="ai")
    check("Python requirements (ai/requirements.txt)", code == 0, out[:200] if out else "")

    # Node deps
    print("  Installing Node.js workspaces...")
    code, out = run(["npm", "install"])
    check("Node.js packages (npm install)", code == 0, out[:200] if out else "")

    # ── Generate proto stubs ──────────────────────────────────────────────
    print("\nProtobuf:")
    code, _ = run([sys.executable, "-m", "grpc_tools.protoc",
                   "-I./proto",
                   "--python_out=.",
                   "--grpc_python_out=.",
                   "./proto/optiflow.proto"], cwd="ai")
    check("gRPC proto stubs generated", code == 0,
          "Install grpcio-tools: pip install grpcio-tools")

    # ── .env ──────────────────────────────────────────────────────────────
    print("\nConfiguration:")
    env_exists = Path(".env").exists()
    if not env_exists:
        import shutil as sh
        sh.copy(".env.example", ".env")
        check(".env created from .env.example", True)
    else:
        check(".env already exists", True)

    # ── Summary ───────────────────────────────────────────────────────────
    print("\n" + "="*60)
    if all_ok:
        print("  ✅  All checks passed! Ready to launch.\n")
        print("  Quick start:")
        print("    docker-compose up          (full stack)")
        print("    optiflow status            (system health)")
        print("    optiflow start <rom.gba>   (launch game + AI)\n")
    else:
        print("  ⚠️  Some checks failed. Fix the issues above and re-run.\n")
        print("  Once fixed: python setup.py\n")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
