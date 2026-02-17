# OpenAI Whisper 技能

一个 Claude Code 技能，根据你的硬件自动选择最优的 Whisper 语音识别实现。

## 功能特性

- **环境检测**：自动检测操作系统、架构和 GPU，推荐最佳 Whisper 实现
- **多实现支持**：涵盖 mlx-whisper、faster-whisper、whisper.cpp 和 openai-whisper
- **安装指南**：针对不同平台的安装说明
- **使用示例**：常见转录模式和输出格式

## 快速开始

```bash
# 检测你的环境
python3 scripts/detect_env.py

# 或在 Claude Code 中调用
/openai-whisper
```

## 决策矩阵

| 环境 | 推荐 | 备选 |
|------|------|------|
| macOS Apple Silicon | mlx-whisper | whisper.cpp |
| macOS Intel | whisper.cpp | faster-whisper |
| Linux + NVIDIA 8GB+ | faster-whisper | insanely-fast-whisper |
| Linux CPU | whisper.cpp | openai-whisper |
| Windows + CUDA | faster-whisper | whisper.cpp |
| Windows CPU | whisper.cpp | openai-whisper |

## 模型推荐

大多数任务使用 `turbo` 模型——它以 8 倍速度提供接近 large-v3 的准确度。

## 文件结构

```
openai-whisper/
├── SKILL.md                    # 主技能文档
├── scripts/
│   └── detect_env.py          # 环境检测脚本
└── .claude/
    └── settings.local.json    # Bash 权限配置
```

## 参考资料

- [OpenAI Whisper](https://github.com/openai/whisper)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [mlx-whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper)
