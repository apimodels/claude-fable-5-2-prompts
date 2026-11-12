# Robot night market short film with procedural sound

Claude Fable 5.2 case 29 of 145 · Three.js Scenes and Animation · [简体中文](#中文)

By [@evaninfra](https://x.com/evaninfra) · [original post](https://x.com/evaninfra/status/2120453048476778687) · posted 2026-11-11 · [watch it in the apimodels.app gallery](https://apimodels.app/claude-fable-5-2-prompts/threejs)

- **What it is:** A 73-second short film set in a robot night market, built in three.js with procedural sound effects. The run took 3 hours 13 minutes.
- **Media:** Video, 79 s. About 53 views and 2 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 674 characters it is excerpted below, with our outline of how the brief is built.
- **Note:** The prompt comes from the author's blog; BRIEF.md itself was not published.

**Prompt (excerpt; full text at the [source](https://tokenbill.tinhdev.com/2026-11-11-making-before-morning.html))**

```text
You are the director of this film. Read BRIEF.md, then make it in this folder.
Plan each shot before you build it.

- Write SHOTPLAN.md first: framing, camera move, light and the sound cue for each shot.
- Keep every number (positions, colours, lights) in one file that all shots import.
[…]
```

**How the brief is built (our outline)**

- Casts the agent as the director and points it at a separate BRIEF.md, not published, that holds the story.
- Asks for SHOTPLAN.md before any building: framing, camera move, light and the sound cue for each shot.
- Keeps every number (positions, colours, lights) in one file that all shots import, and asks for a command that renders one shot's stills in under 30 seconds.
- Builds in two approval stops: after one finished reference shot (four stills), and after a grey pass of every shot with sound.
- Ends with self-review: stills from every shot and both sides of every cut, then a RESULT.md listing what was wrong and what still does not work.

To make one like it: the [Three.js starter](../../starter/threejs) turns a page with renderAt(t) into an MP4 (tested), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**73 秒机器人夜市短片**

作者：[@evaninfra](https://x.com/evaninfra) · [原帖](https://x.com/evaninfra/status/2120453048476778687) · 发布于 2026-11-11 · [在 apimodels.app 案例库看成片](https://apimodels.app/zh/claude-fable-5-2-prompts/threejs)

- **作品：** 73 秒机器人夜市短片，three.js 加程序化音效，跑了 3 小时 13 分钟。
- **媒体：** 视频 79 秒。截至 2026-11-11 约 53 浏览、2 赞。
- **提示词：** 作者公开了原文，全文 674 个字符，上方只放节选，下面是我们整理的结构说明。
- **备注：** 提示词取自作者博客；BRIEF.md 本身没公开。

**这份提示词的结构（我们整理）**

- 让 agent 当导演，故事放在另一个 BRIEF.md 里（没公开）。
- 动手前先写 SHOTPLAN.md：每个镜头的构图、运镜、光线和声音提示点。
- 所有数字（位置、颜色、灯光）放在一个文件里供各镜头引用；还要做一条命令，30 秒内渲出单个镜头的静帧。
- 设两个审批点：做完一个参考镜头后给 4 张静帧等确认；所有镜头灰模加声音过一遍后给视频等确认。
- 收尾要自查：看每个镜头和每个剪辑点前后两侧的静帧，再写 RESULT.md，列出每个镜头哪里有问题、哪些还没解决。

想做类似的：[Three.js 起步脚本](../../starter/threejs)把带 renderAt(t) 的网页逐帧转成 MP4（实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Voxel Paris as a 14-second three.js animation](028-voxel-paris-as-a-14-second-three-js-animation.md) · [All 145 cases](../../README.md) · [Interactive Stonehenge winter solstice sunrise in three.js](030-interactive-stonehenge-winter-solstice-sunrise-in-three-js.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
