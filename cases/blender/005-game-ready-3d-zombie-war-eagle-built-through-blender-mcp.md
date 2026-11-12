# Game-ready 3D zombie war eagle built through Blender MCP

Claude Fable 5.2 case 5 of 145 · Blender 3D with Python · [简体中文](#中文)

By [@maxt3chno](https://x.com/maxt3chno) · [original post](https://x.com/maxt3chno/status/2119896698281467952) · posted 2026-11-09 · [watch it in the apimodels.app gallery](https://apimodels.app/claude-fable-5-2-prompts/blender)

- **What it is:** A game-ready 3D zombie war eagle built through Blender MCP and matched to a reference image part by part.
- **Media:** Video, 21 s. About 21K views and 304 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 9,411 characters it is excerpted below, with our outline of how the brief is built.

**Prompt (excerpt; full text at the [source](https://x.com/maxt3chno/status/2119896909062058411))**

```text
You are building a game-ready 3D creature in Blender through Blender MCP (execute_blender_code for actions, renders and viewport screenshots to check your work). The attached image is the reference. Goal: an outstanding, realistic, production-quality model that matches the reference as closely as possible.
[…]
```

**How the brief is built (our outline)**

- Sets up the agent before the art: which Blender MCP tools to use, a working folder, a saved .blend after every stage, and "never ask me questions": when unsure, pick whatever is closest to the reference and continue.
- WHAT IT IS gives size, units and orientation (about 1.6 m tall hunched, about 4.2 m wingspan, metres, facing -Y, feet at Z = 0) and asks for a static model in the reference pose, with no rig and no animation.
- THE REFERENCE, PART BY PART walks through the skull, beak, eyes (one blind, with a scar cut into the geometry), body, shoulder wound, wings and the natural and mechanical legs, naming sides as "its left (right side of the image)" so they cannot be confused.
- HOW TO BUILD IT orders the work: a blockout against an orthographic reference camera, a subdivision-ready body mesh, feathers from a 2048 px atlas of 10-16 feathers it draws itself in numpy (flagged as the step that decides the look), the wound, both legs, then PBR materials.
- CHECKS, GAME LIMITS and OUTPUT close it: at most 80,000 triangles and 4 texture sets of 2048 px, a GLB under 30 MB with named objects, six named renders including one beside the reference, and a short report.

To make one like it: the [Blender starter](../../starter/blender) renders a scene from Python (tested on Blender 5.3), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**Blender MCP 做的游戏级僵尸战鹰**

作者：[@maxt3chno](https://x.com/maxt3chno) · [原帖](https://x.com/maxt3chno/status/2119896698281467952) · 发布于 2026-11-09 · [在 apimodels.app 案例库看成片](https://apimodels.app/zh/claude-fable-5-2-prompts/blender)

- **作品：** 通过 Blender MCP 做出的游戏级 3D 僵尸战鹰，对照参考图逐部位建模。
- **媒体：** 视频 21 秒。截至 2026-11-11 约 2.1 万 浏览、304 赞。
- **提示词：** 作者公开了原文，全文 9,411 个字符，上方只放节选，下面是我们整理的结构说明。

**这份提示词的结构（我们整理）**

- 先把 agent 的工作方式交代清楚：用哪些 Blender MCP 工具、工作目录在哪、每个阶段存一个 .blend，并且「不要问我问题」：拿不准就选最接近参考图的做法继续。
- WHAT IT IS 给出尺寸、单位和朝向（弓背时约 1.6 米高、翼展约 4.2 米、单位米、面朝 -Y、脚在 Z = 0），要求做参考图姿势的静态模型，不绑定、不做动画。
- THE REFERENCE, PART BY PART 逐部位描述：头骨、喙、眼睛（一只瞎眼，伤疤要真的切进几何体）、身体、肩部伤口、翅膀、真腿和机械腿；左右一律写成「它的左边（图的右边）」，避免搞反。
- HOW TO BUILD IT 规定顺序：对着正交参考相机做大形 → 可细分的身体网格 → 羽毛（自己用 numpy 画 10–16 种羽毛拼成 2048 px 贴图集，明确说这一步决定整体观感）→ 伤口 → 两条腿 → PBR 材质。
- 最后是 CHECKS、GAME LIMITS 和 OUTPUT：总面数不超过 80,000 个三角面、最多 4 套 2048 px 贴图、GLB 小于 30 MB 且对象按规定命名，输出 6 张指定角度的渲染图（含一张和参考图并排），再附一份简短报告。

想做类似的：[Blender 起步脚本](../../starter/blender)用 Python 建场景并渲染（Blender 5.3 实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Steam locomotive transforms into a robot in a 2D anime short](004-steam-locomotive-transforms-into-a-robot-in-a-2d-anime-short.md) · [All 145 cases](../../README.md) · [Jerusalem in the final week of Jesus's life, rebuilt in Blender](006-jerusalem-in-the-final-week-of-jesus-s-life-rebuilt-in.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
