# OpenAI Whisper 指南

根据你的硬件自动选择最优的 Whisper 语音识别实现。适用于 Claude Code 和 Opencode。

## 功能特性

- **环境检测**：自动检测操作系统、架构和 GPU，推荐最佳 Whisper 实现
- **多实现支持**：涵盖 mlx-whisper、faster-whisper、whisper.cpp 和 openai-whisper
- **安装指南**：针对不同平台的安装说明
- **使用示例**：常见转录模式和输出格式

## 快速开始

本技能适用于 [Claude Code](https://claude.ai/claude-code) 或 [Opencode](https://github.com/opencode-ai/opencode)。只需告诉 Claude：

> "转录这个音频文件"
>
> "把 video.mp4 转成 SRT 字幕"
>
> "我的 Mac 适合用哪个 Whisper？"
>
> "安装 whisper 并转录 podcast.mp3"

或直接调用 `/openai-whisper-guide`。

```bash
# 检测你的环境
python3 scripts/detect_env.py
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
openai-whisper-guide/
├── SKILL.md                    # 主文档
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

## 许可证

MIT

## 支持

如果这个项目对你有帮助，欢迎支持作者：

<table>
  <tr>
    <td align="center">
      <img src="images/wechat-pay.png" width="180" alt="微信支付">
      <br>
      <b>微信支付</b>
    </td>
    <td align="center">
      <img src="images/alipay.png" width="180" alt="支付宝">
      <br>
      <b>支付宝</b>
    </td>
  </tr>
</table>

## 作者

**探索未至之境**

- Bilibili: https://space.bilibili.com/441831884
- GitHub: https://github.com/Agents365-ai
