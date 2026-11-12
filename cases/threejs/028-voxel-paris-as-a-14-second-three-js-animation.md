# Voxel Paris as a 14-second three.js animation

Claude Fable 5.2 case 28 of 145 · Three.js Scenes and Animation · [简体中文](#中文)

By [@RezAIT00](https://x.com/RezAIT00) · [original post](https://x.com/RezAIT00/status/2119894257519767656) · posted 2026-11-09 · [watch it in the apimodels.app gallery](https://apimodels.app/claude-fable-5-2-prompts/threejs)

- **What it is:** Paris in voxel style, animated for 14 seconds on a single three.js page.
- **Media:** Video, 14 s. About 4,436 views and 41 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 1,859 characters it is excerpted below, with our outline of how the brief is built.
- **Note:** The author credits the prompt to @semichenkko.

**Prompt (excerpt; full text at the [source](https://x.com/RezAIT00/status/2119898136894156960))**

```text
Build a single self-contained three.js HTML page that renders a 14-second animation (1280x720, 30fps, deterministic: expose window.renderAt(t) so every frame can be captured).  Scene: a floating voxel diorama island - Paris, 1888, the Eiffel Tower under construction. Everything is already moving on frame 1.  Island:
[…]
```

**How the brief is built (our outline)**

- The first line is a build contract: one self-contained three.js page, a 14-second animation at 1280x720 and 30 fps, deterministic, exposing window.renderAt(t) so any frame can be captured.
- The scene is a floating voxel island: Paris in 1888 with the Eiffel Tower under construction, and everything already moving on frame 1.
- The tower gets the most detail: dark wrought-iron lattice made of thin voxel beams with real X-bracing, "not solid blocks", built level by level with scaffolding, cranes and rivet sparks.
- A "life" list fills the island: hundreds of people about 3 voxels tall, cranes, horse-drawn carts, a riverboat, carriages and pigeons.
- Camera and look close it: a slow orbit of about 25 degrees with a push-in, late-afternoon sun, ambient occlusion, haze, ACES tone mapping and bloom on the sparks.

To make one like it: the [Three.js starter](../../starter/threejs) turns a page with renderAt(t) into an MP4 (tested), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**体素风巴黎 14 秒 three.js 动画**

作者：[@RezAIT00](https://x.com/RezAIT00) · [原帖](https://x.com/RezAIT00/status/2119894257519767656) · 发布于 2026-11-09 · [在 apimodels.app 案例库看成片](https://apimodels.app/zh/claude-fable-5-2-prompts/threejs)

- **作品：** 体素风巴黎，14 秒 three.js 单页动画。
- **媒体：** 视频 14 秒。截至 2026-11-11 约 4,436 浏览、41 赞。
- **提示词：** 作者公开了原文，全文 1,859 个字符，上方只放节选，下面是我们整理的结构说明。
- **备注：** 作者注明提示词来自 @semichenkko。

**这份提示词的结构（我们整理）**

- 第一句就是交付约定：一个自包含的 three.js 单页，14 秒动画，1280x720、30 fps，必须确定性，暴露 window.renderAt(t)，任意一帧都能截下来。
- 场景是一座漂浮的体素小岛：1888 年的巴黎，埃菲尔铁塔正在施工，第 1 帧起一切就在动。
- 铁塔写得最细：深色熟铁桁架用细体素梁搭，要有真正的 X 形斜撑，不能是实心方块；按层写施工进度，配脚手架、吊车和铆接火花。
- 「生活」清单把岛填满：几百个约 3 体素高的小人、吊车、马车、河上的汽船、过桥的马车和鸽子。
- 最后是镜头和画面：约 25 度的缓慢环绕加推近，傍晚暖阳、环境光遮蔽、薄雾、ACES 色调映射、火花带辉光。

想做类似的：[Three.js 起步脚本](../../starter/threejs)把带 renderAt(t) 的网页逐帧转成 MP4（实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [83-second animated short rendered frame by frame in three.js](027-83-second-animated-short-rendered-frame-by-frame-in-three-js.md) · [All 145 cases](../../README.md) · [Robot night market short film with procedural sound](029-robot-night-market-short-film-with-procedural-sound.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
