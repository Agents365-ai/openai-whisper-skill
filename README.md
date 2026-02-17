# OpenAI Whisper Guide

[中文文档](README_CN.md)

A guide for automatic speech recognition using the optimal Whisper implementation for your hardware. Works with Claude Code and Opencode.

## Features

- **Environment Detection**: Automatically detects your OS, architecture, and GPU to recommend the best Whisper implementation
- **Multi-Implementation Support**: Covers mlx-whisper, faster-whisper, whisper.cpp, and openai-whisper
- **Installation Guides**: Platform-specific installation instructions
- **Usage Examples**: Common transcription patterns and output formats

## Quick Start

This skill is designed for use with [Claude Code](https://claude.ai/claude-code) or [Opencode](https://github.com/opencode-ai/opencode). Simply tell Claude:

> "Transcribe this audio file"
>
> "Convert video.mp4 to SRT subtitles"
>
> "What's the best Whisper for my Mac?"
>
> "Install whisper and transcribe podcast.mp3"

Or invoke directly with `/openai-whisper-guide`.

```bash
# Detect your environment
python3 scripts/detect_env.py
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
openai-whisper-guide/
├── SKILL.md                    # Main documentation
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

## License

MIT

## Support

If this project helps you, consider supporting the author:

<table>
  <tr>
    <td align="center">
      <img src="images/wechat-pay.png" width="180" alt="WeChat Pay">
      <br>
      <b>WeChat Pay</b>
    </td>
    <td align="center">
      <img src="images/alipay.png" width="180" alt="Alipay">
      <br>
      <b>Alipay</b>
    </td>
  </tr>
</table>

## Author

**探索未至之境**

- Bilibili: https://space.bilibili.com/441831884
- GitHub: https://github.com/Agents365-ai
