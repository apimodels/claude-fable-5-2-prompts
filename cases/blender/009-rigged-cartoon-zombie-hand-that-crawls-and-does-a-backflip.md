# Rigged cartoon zombie hand that crawls and does a backflip

Claude Fable 5.2 case 9 of 145 · Blender 3D with Python · [简体中文](#中文)

By [@higgsfield_ai](https://x.com/higgsfield_ai) · [original post](https://x.com/higgsfield_ai/status/2119893970897490135) · posted 2026-11-09

- **What it is:** From Higgsfield: a rigged zombie hand built with Blender Python that crawls and does a backflip, with the keyframes refined in stages.
- **Media:** Video, 19 s. About 63K views and 950 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 8,138 characters it is excerpted below, with our outline of how the brief is built.
- **Note:** The prompt is transcribed from a third-party repository, [github.com/yihui-dev/awesome-fable5-2-videos](https://github.com/yihui-dev/awesome-fable5-2-videos), which cites the Higgsfield blog as its source; this page shows only an excerpt.

**Prompt (excerpt; full text at the [source](https://higgsfield.ai/blog))**

```text
Using Blender's Python API (bpy, bmesh, mathutils), build a complete animation pipeline from scratch and get it right on the first pass:

1. Model an original stylized cartoon zombie hand with stylized wounds, stitches and a severed stump at the wrist.
2.
[…]
```

**How the brief is built (our outline)**

- Opens with a five-step pipeline in Blender's Python API, to be right on the first pass: model an original cartoon zombie hand, build a production-style rig with custom controllers (IK/FK, gizmo rings, curl sliders), animate it, shade and light it, and render on a cloud GPU.
- Modelling covers the silhouette, the zombie details on the back of the hand and the stump, and animation-ready topology.
- Animation runs in two passes: key-pose blocking first, then curve polish in the Graph Editor for overlap, weight and floor contact.
- The output is one 20-second, 1920×1080 video that shows both the rig and the render.
- Before the full render it must render six check frames locally (including the mid-air backflip and a pose with the controllers visible) and review each one for twisted fingers, torn mesh and loose wounds.
- The cloud render has a cost gate: list GPUs and prices, check nothing is already running, quote the job with expected and maximum credits, and start only after a yes; then follow the job until there is a finished video.

To make one like it: the [Blender starter](../../starter/blender) renders a scene from Python (tested on Blender 5.3), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**会爬行和后空翻的僵尸手动画**

作者：[@higgsfield_ai](https://x.com/higgsfield_ai) · [原帖](https://x.com/higgsfield_ai/status/2119893970897490135) · 发布于 2026-11-09

- **作品：** Higgsfield：Blender Python 做出绑定好的僵尸手，会爬行、会后空翻（含关键帧分阶段打磨）。
- **媒体：** 视频 19 秒。截至 2026-11-11 约 6.3 万 浏览、950 赞。
- **提示词：** 作者公开了原文，全文 8,138 个字符，上方只放节选，下面是我们整理的结构说明。
- **备注：** 提示词转录自第三方仓库 [github.com/yihui-dev/awesome-fable5-2-videos](https://github.com/yihui-dev/awesome-fable5-2-videos)（来源为 Higgsfield 博客），本页只放节选。

**这份提示词的结构（我们整理）**

- 开头列出一条 5 步流程，全用 Blender 的 Python API，要求一次做对：建一只原创卡通僵尸手 → 做带自定义控制器的生产级绑定（IK/FK、圈形控制器、弯曲滑杆）→ 做动画 → 材质灯光 → 用云端 GPU 渲染。
- 建模部分写了剪影比例、手背和断腕处的僵尸细节，以及适合做动画的布线。
- 动画分两遍：先摆关键姿势，再到 Graph Editor 里打磨曲线，处理跟随、重量感和触地。
- 成片是一支 20 秒、1920×1080 的视频，同时展示绑定和渲染效果。
- 全片渲染前，先在本地渲 6 张检查帧（包括空中后空翻、露出控制器的姿势），逐张检查手指有没有扭成怪角度、网格有没有破、伤口贴不贴皮。
- 云端渲染前设了花钱关卡：先列出 GPU 型号和价格、确认没有自己的任务在跑，报出预计和最多花多少积分，等「同意」才开始；之后一直跟到拿到成片。

想做类似的：[Blender 起步脚本](../../starter/blender)用 Python 建场景并渲染（Blender 5.3 实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Star Wars Blender Bench: the First Battle of Geonosis](008-star-wars-blender-bench-the-first-battle-of-geonosis.md) · [All 145 cases](../../README.md) · [Transformer truck with an animation of it transforming](010-transformer-truck-with-an-animation-of-it-transforming.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
