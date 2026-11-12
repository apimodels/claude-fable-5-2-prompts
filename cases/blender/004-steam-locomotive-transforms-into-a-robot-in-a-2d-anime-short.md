# Steam locomotive transforms into a robot in a 2D anime short

Claude Fable 5.2 case 4 of 145 · Blender 3D with Python · [简体中文](#中文)

By [@0kncn](https://x.com/0kncn) · [original post](https://x.com/0kncn/status/2119901782482543073) · posted 2026-11-09

- **What it is:** A 90-second short in the style of 2D Japanese anime, in which a steam locomotive transforms into a robot. Everything was built in Blender with Python and rendered in Eevee with line art, and even the score was written in code, synthesized with numpy oscillators (see [x.com/0kncn/status/2120060332194287853](https://x.com/0kncn/status/2120060332194287853)).
- **Media:** Video, 90 s. About 69K views and 410 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 6,390 characters it is excerpted below, with our outline of how the brief is built.

**Prompt (excerpt; full text at the [source](https://x.com/0kncn/status/2119901786060259612))**

```text
Create a 2D anime short. It must look completely like real Japanese anime, as if it were taken directly from a finished theatrical anime film. This is traditional-looking, hand-drawn 2D anime, not a 3D animation, a moving illustration, or a stylized web graphic.
[…]
```

**How the brief is built (our outline)**

- Opens with the deliverable and the bar: one 90-second MP4 at 1920x1080 and 24 fps that must look like hand-drawn theatrical 2D anime, built in Blender from Python, rendered in Eevee, then inked and painted frame by frame in a second pass, with a synthesized soundtrack.
- HERO fixes the design with hard numbers: a 1940s 2-8-2 freight locomotive 23 m long that becomes a 21 m robot, down to the rust, the moss and a stork's nest on the cab roof, and requires an original design.
- TRANSFORM splits one 120-frame transformation into five 24-frame stages and rules out cheating: every part is rigid, nothing stretches, vanishes or appears, and each piece moves on a hinge or slide you can see.
- WORLD and STORY lay out a real-scale mountain railway (a 126 m viaduct of seven 18 m spans) and the plot beat by beat, from the rockfall to the robot staying behind as the new pier.
- LIGHT and SOUND set the look (high-key cel light, gouache backgrounds, effects drawn on twos, no particle mush) and a 144 bpm grid where every cut lands on a multiple of 5 frames and 16 music hits land on picture.
- FORMAT asks for a Python "story clock" with one state per frame; CHECKS has a script test every frame for parts passing through each other, wheel slip, sliding feet and the camera entering a mesh before the final render.

To make one like it: the [Blender starter](../../starter/blender) renders a scene from Python (tested on Blender 5.3), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**蒸汽机车变形成机器人的 2D 动画短片**

作者：[@0kncn](https://x.com/0kncn) · [原帖](https://x.com/0kncn/status/2119901782482543073) · 发布于 2026-11-09

- **作品：** 90 秒 2D 日式动画风短片：蒸汽机车变形成机器人。全部在 Blender 里用 Python 搭建，Eevee 渲染加描线；配乐也是代码写的（numpy 振荡器合成，见 [x.com/0kncn/status/2120060332194287853](https://x.com/0kncn/status/2120060332194287853)）。
- **媒体：** 视频 90 秒。截至 2026-11-11 约 6.9 万 浏览、410 赞。
- **提示词：** 作者公开了原文，全文 6,390 个字符，上方只放节选，下面是我们整理的结构说明。

**这份提示词的结构（我们整理）**

- 开头先交代交付物和标准：一支 90 秒、1920x1080、24 fps 的 MP4，必须看起来就是院线级手绘 2D 日本动画；在 Blender 里用 Python 搭，Eevee 渲染，再逐帧做第二遍描线上色，配乐也要合成出来。
- HERO 段用具体数字定死设计：1940 年代 2-8-2 货运机车，长 23 米，变成机器人后高 21 米，连锈迹、苔藓和驾驶室顶上的鹳鸟窝都写了，并要求是原创设计。
- TRANSFORM 段把一次 120 帧的变形拆成 5 段、每段 24 帧，并且堵死偷懒的路：所有零件都是刚体，不能拉伸、消失或凭空出现，每一块都沿看得见的铰链或滑轨移动。
- WORLD 和 STORY 段给出真实比例的山区铁路（7 跨、每跨 18 米、全长 126 米的高架桥）和逐拍剧情，从落石一直写到机器人留下来当新桥墩。
- LIGHT 和 SOUND 段定画风（高调赛璐珞光、水粉背景、特效一拍二手绘、不要粒子糊）和 144 bpm 的节拍网格：每个剪辑点落在 5 帧的整数倍上，16 个音乐重音对准画面。
- FORMAT 要求写成 Python「故事时钟」，每帧一个状态；CHECKS 要求最终渲染前用脚本逐帧检查穿模、车轮打滑、脚底滑步和镜头穿进模型。

想做类似的：[Blender 起步脚本](../../starter/blender)用 Python 建场景并渲染（Blender 5.3 实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [13-shot Blender short with a MacBook and Clawd, made on a livestream](003-13-shot-blender-short-with-a-macbook-and-clawd-made-on-a.md) · [All 145 cases](../../README.md) · [Game-ready 3D zombie war eagle built through Blender MCP](005-game-ready-3d-zombie-war-eagle-built-through-blender-mcp.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
