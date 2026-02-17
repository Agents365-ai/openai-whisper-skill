# OpenAI Whisper Skill

A Claude Code skill for automatic speech recognition using the optimal Whisper implementation for your hardware.

## Features

- **Environment Detection**: Automatically detects your OS, architecture, and GPU to recommend the best Whisper implementation
- **Multi-Implementation Support**: Covers mlx-whisper, faster-whisper, whisper.cpp, and openai-whisper
- **Installation Guides**: Platform-specific installation instructions
- **Usage Examples**: Common transcription patterns and output formats

## Quick Start

```bash
# Detect your environment
python3 scripts/detect_env.py

# Or invoke in Claude Code
/openai-whisper
```

## Decision Matrix

| Environment | Recommended | Alternative |
|-------------|-------------|-------------|
| macOS Apple Silicon | mlx-whisper | whisper.cpp |
| macOS Intel | whisper.cpp | faster-whisper |
| Linux + NVIDIA 8GB+ | faster-whisper | insanely-fast-whisper |
| Linux CPU | whisper.cpp | openai-whisper |
| Windows + CUDA | faster-whisper | whisper.cpp |
| Windows CPU | whisper.cpp | openai-whisper |

## Model Recommendation

Use `turbo` model for most tasks—it offers near large-v3 accuracy at 8x speed.

## File Structure

```
openai-whisper/
├── SKILL.md                    # Main skill documentation
├── scripts/
│   └── detect_env.py          # Environment detection
└── .claude/
    └── settings.local.json    # Bash permissions
```

## References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [mlx-whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
