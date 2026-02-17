#!/usr/bin/env python3
"""Detect environment and recommend optimal Whisper implementation."""
import json, platform, subprocess, shutil

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True).strip()
    except:
        return ""

def detect():
    os_name = platform.system().lower()
    arch = platform.machine().lower()

    # Normalize architecture
    if arch in ("arm64", "aarch64"):
        arch = "arm64"
    elif arch in ("x86_64", "amd64"):
        arch = "x86_64"

    gpu = {"type": "none", "name": None, "vram_gb": None}

    # Detect GPU
    if os_name == "darwin":
        if arch == "arm64":
            chip = run("sysctl -n machdep.cpu.brand_string")
            # Estimate unified memory
            mem = run("sysctl -n hw.memsize")
            vram = int(mem) // (1024**3) if mem.isdigit() else 8
            gpu = {"type": "apple_silicon", "name": chip or "Apple Silicon", "vram_gb": vram}
    elif shutil.which("nvidia-smi"):
        nv = run("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader,nounits")
        if nv:
            parts = nv.split(",")
            name = parts[0].strip() if parts else "NVIDIA"
            vram = int(parts[1].strip()) // 1024 if len(parts) > 1 else None
            gpu = {"type": "nvidia", "name": name, "vram_gb": vram}

    # Determine recommendation
    rec, alt = recommend(os_name, arch, gpu)

    return {
        "os": os_name,
        "arch": arch,
        "gpu": gpu,
        "recommended": rec,
        "alternative": alt,
        "install_cmd": get_install_cmd(rec, os_name),
    }

def recommend(os_name, arch, gpu):
    if os_name == "darwin":
        if gpu["type"] == "apple_silicon":
            return "mlx-whisper", "whisper.cpp"
        return "whisper.cpp", "faster-whisper"

    if gpu["type"] == "nvidia":
        vram = gpu.get("vram_gb") or 0
        if vram >= 8:
            return "faster-whisper", "insanely-fast-whisper"
        return "faster-whisper", "whisper.cpp"

    # CPU fallback
    return "whisper.cpp", "openai-whisper"

def get_install_cmd(impl, os_name):
    cmds = {
        "mlx-whisper": "pip install mlx-whisper",
        "faster-whisper": "pip install faster-whisper",
        "whisper.cpp": "brew install whisper-cpp" if os_name == "darwin" else "# Build from source: https://github.com/ggml-org/whisper.cpp",
        "openai-whisper": "pip install -U openai-whisper",
        "insanely-fast-whisper": "pip install insanely-fast-whisper",
    }
    return cmds.get(impl, "")

if __name__ == "__main__":
    print(json.dumps(detect(), indent=2))
