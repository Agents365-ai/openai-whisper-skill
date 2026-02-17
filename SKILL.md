---
name: openai-whisper-guide
description: Use when transcribing audio/video to text, installing speech recognition, or detecting hardware for optimal Whisper implementation. Covers openai-whisper, whisper.cpp, faster-whisper, mlx-whisper.
user_invocable: true
---

# OpenAI Whisper Guide

Automatic speech recognition using the optimal Whisper implementation for your hardware.

## Quick Start

Detect your environment and get recommendations:

```bash
python3 ~/.claude/skills/openai-whisper/scripts/detect_env.py
```

## Environment Detection

### Manual Detection

```bash
# OS and architecture
uname -ms

# macOS: Check for Apple Silicon
sysctl -n machdep.cpu.brand_string

# Linux/Windows: Check NVIDIA GPU
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
```

## Implementation Decision Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                    Which Whisper to Use?                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  macOS?           │
                    └─────────┬─────────┘
                    yes │           │ no
              ┌─────────▼───────┐   │
              │ Apple Silicon?  │   │
              └────────┬────────┘   │
              yes │        │ no     │
                  ▼        ▼        │
           ┌──────────┐ ┌────────┐  │
           │mlx-whisper│ │whisper │  │
           │ (fastest) │ │  .cpp  │  │
           └──────────┘ └────────┘  │
                                    │
                    ┌───────────────▼───────────────┐
                    │         NVIDIA GPU?           │
                    └───────────────┬───────────────┘
                           yes │           │ no
                    ┌──────────▼──────────┐│
                    │   VRAM >= 8GB?      ││
                    └──────────┬──────────┘│
                    yes │           │ no   │
                        ▼           ▼      ▼
                 ┌──────────┐ ┌────────┐ ┌────────┐
                 │ faster-  │ │faster- │ │whisper │
                 │ whisper  │ │whisper │ │  .cpp  │
                 │or insane │ │        │ │        │
                 └──────────┘ └────────┘ └────────┘
```

## Implementations Comparison

| Implementation | Best For | Speed | Install |
|----------------|----------|-------|---------|
| **mlx-whisper** | Apple Silicon | 🚀🚀🚀 | `pip install mlx-whisper` |
| **faster-whisper** | NVIDIA GPU | 🚀🚀🚀 | `pip install faster-whisper` |
| **insanely-fast-whisper** | High-end NVIDIA | 🚀🚀🚀🚀 | `pip install insanely-fast-whisper` |
| **whisper.cpp** | CPU / Low RAM | 🚀🚀 | `brew install whisper-cpp` |
| **openai-whisper** | Universal fallback | 🚀 | `pip install -U openai-whisper` |

## Installation

### mlx-whisper (macOS Apple Silicon)

```bash
pip install mlx-whisper

# Transcribe
mlx_whisper audio.mp3 --model mlx-community/whisper-turbo
```

### faster-whisper (NVIDIA GPU)

```bash
pip install faster-whisper

# Python usage
from faster_whisper import WhisperModel
model = WhisperModel("turbo", device="cuda", compute_type="float16")
segments, info = model.transcribe("audio.mp3")
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
```

### whisper.cpp (CPU / Cross-platform)

```bash
# macOS
brew install whisper-cpp

# Download model
whisper-cpp-download-ggml-model turbo

# Transcribe (requires 16kHz WAV)
ffmpeg -i audio.mp3 -ar 16000 -ac 1 audio.wav
whisper-cpp -m ~/.whisper/ggml-turbo.bin -f audio.wav -otxt
```

### openai-whisper (Original)

```bash
pip install -U openai-whisper

# Transcribe
whisper audio.mp3 --model turbo --output_format srt
```

### insanely-fast-whisper (High-end NVIDIA)

```bash
pip install insanely-fast-whisper

# Transcribe with batched inference
insanely-fast-whisper --file-name audio.mp3 --model-name openai/whisper-large-v3 --batch-size 24
```

## Model Sizes

| Model | VRAM | Relative Speed | Best For |
|-------|------|----------------|----------|
| `tiny` | ~1GB | 10x | Quick drafts, testing |
| `base` | ~1GB | 7x | Good quality, fast |
| `small` | ~2GB | 4x | Balanced |
| `medium` | ~5GB | 2x | High accuracy |
| **`turbo`** | ~6GB | **8x** | **Best balance** ⭐ |
| `large-v3` | ~10GB | 1x | Maximum accuracy |

**Recommendation:** Use `turbo` for most tasks. It offers near large-v3 accuracy at 8x speed.

## Common Usage Patterns

### Basic Transcription

```bash
# mlx-whisper
mlx_whisper audio.mp3

# faster-whisper (Python)
python -c "
from faster_whisper import WhisperModel
model = WhisperModel('turbo', device='cuda')
for seg, _ in model.transcribe('audio.mp3'):
    print(seg.text)
"

# openai-whisper
whisper audio.mp3 --model turbo
```

### Generate SRT Subtitles

```bash
# openai-whisper
whisper audio.mp3 --model turbo --output_format srt

# mlx-whisper
mlx_whisper audio.mp3 --output-format srt
```

### Subtitle Formatting (Whisper Native)

Control line width and count for better readability:

```bash
# openai-whisper - recommended for professional subtitles
whisper audio.mp3 --model turbo --output_format srt \
  --max_line_width 42 \
  --max_line_count 2

# faster-whisper (Python)
from faster_whisper import WhisperModel
model = WhisperModel("turbo")
segments, _ = model.transcribe(
    "audio.mp3",
    max_line_width=42,
    max_line_count=2,
)
```

| Parameter | Recommended | Description |
|-----------|-------------|-------------|
| `--max_line_width` | 42 | Max characters per line |
| `--max_line_count` | 2 | Max lines per subtitle |
| `--max_words_per_line` | 8 | Max words per line |

> **Note:** For Netflix-quality subtitles (timing, reading speed, gaps), additional post-processing is needed beyond Whisper's native capabilities.

### Transcribe with Language Detection

```bash
# Auto-detect language
whisper audio.mp3 --model turbo

# Force language
whisper audio.mp3 --model turbo --language en
```

### Word-Level Timestamps (WhisperX)

```bash
pip install whisperx

whisperx audio.mp3 --model large-v3 --align_model WAV2VEC2_ASR_LARGE_LV60K_960H
```

## Output Formats

| Format | Flag | Use Case |
|--------|------|----------|
| TXT | `--output_format txt` | Plain text |
| SRT | `--output_format srt` | Subtitles |
| VTT | `--output_format vtt` | Web subtitles |
| JSON | `--output_format json` | Programmatic |
| TSV | `--output_format tsv` | Spreadsheet |

## Troubleshooting

### "CUDA out of memory"

Use a smaller model or reduce batch size:
```bash
# Smaller model
whisper audio.mp3 --model small

# Or use CPU
whisper audio.mp3 --model turbo --device cpu
```

### Slow on Apple Silicon

Ensure you're using mlx-whisper, not openai-whisper:
```bash
pip uninstall openai-whisper
pip install mlx-whisper
```

### whisper.cpp: "Invalid WAV format"

Convert to 16kHz mono WAV:
```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

### Poor transcription quality

1. Try a larger model (`medium` or `large-v3`)
2. Ensure audio quality is good (reduce noise with ffmpeg)
3. Specify language explicitly with `--language`

### "Model not found"

Download the model first:
```bash
# openai-whisper downloads automatically
# whisper.cpp needs manual download
whisper-cpp-download-ggml-model turbo

# mlx-whisper downloads from HuggingFace
mlx_whisper --model mlx-community/whisper-turbo audio.mp3
```

## References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [mlx-whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
- [WhisperX](https://github.com/m-bain/whisperX)
- [Choosing Whisper Variants](https://modal.com/blog/choosing-whisper-variants)
