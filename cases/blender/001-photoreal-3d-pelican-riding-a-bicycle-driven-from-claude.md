# Photoreal 3D pelican riding a bicycle, driven from Claude Code

Claude Fable 5.2 case 1 of 145 · Blender 3D with Python · [简体中文](#中文)

By [@techfren](https://x.com/techfren) · [original post](https://x.com/techfren/status/2119924958134702276) · posted 2026-11-09

- **What it is:** A photoreal short of a 3D pelican riding a bicycle. Fable 5.2 drove Blender 5.2.3 headlessly from Claude Code, writing about 4,800 lines of Python for a 21-bone rig, feathers and a drivetrain that actually turns, and Cycles OptiX rendered the 444 frames on an RTX 5080 in 56 minutes (technical details in the author's reply, [x.com/techfren/status/2119926681716834440](https://x.com/techfren/status/2119926681716834440)).
- **Media:** Video, 18 s. About 163K views and 910 likes as of 11 November 2026.
- **Prompt:** published by the creator, quoted in full below.
- **Note:** The prompt comes from the full session trace the author published as a Hugging Face dataset; a block of runtime-environment constraints that follows it is not included here. The author also posted a "receipts" post: [x.com/techfren/status/2120203574483550694](https://x.com/techfren/status/2120203574483550694).

**Prompt (the creator's own words)** · [source](https://huggingface.co/datasets/techfren/pelican-fable-trace)

```text
Make a video of a 3D pelican riding a bicycle, as realistic as you can make it: believable anatomy and feathers, a real bicycle with working drivetrain motion, physically plausible riding animation, real-world lighting and camera. Take the time it needs. Deliver a finished video file.
```

To make one like it: the [Blender starter](../../starter/blender) renders a scene from Python (tested on Blender 5.3), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**写实 3D 鹈鹕骑自行车短片**

作者：[@techfren](https://x.com/techfren) · [原帖](https://x.com/techfren/status/2119924958134702276) · 发布于 2026-11-09

- **作品：** 3D 鹈鹕骑自行车写实短片。Fable 5.2 在 Claude Code 里无界面驱动 Blender 5.2.3，写约 4,800 行 Python：21 骨骼绑定、羽毛、可转动的传动系统，Cycles OptiX 在 RTX 5080 上渲 444 帧共 56 分钟（技术细节见作者回复 [x.com/techfren/status/2119926681716834440](https://x.com/techfren/status/2119926681716834440)）。
- **媒体：** 视频 18 秒。截至 2026-11-11 约 16.3 万 浏览、910 赞。
- **提示词：** 作者公开了原文，完整引用见上方代码块。
- **备注：** 提示词取自作者公开的完整会话轨迹（HF 数据集），其后还有一段运行环境约束未收录；作者另发了"收据"帖 [x.com/techfren/status/2120203574483550694](https://x.com/techfren/status/2120203574483550694)。

想做类似的：[Blender 起步脚本](../../starter/blender)用 Python 建场景并渲染（Blender 5.3 实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

[All 145 cases](../../README.md) · [Prehistoric watering hole with dinosaurs, built in Blender with Python](002-prehistoric-watering-hole-with-dinosaurs-built-in-blender.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
