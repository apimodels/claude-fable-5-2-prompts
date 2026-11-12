# One-shot 3D basketball arena game in three.js

Claude Fable 5.2 case 78 of 145 · Games · [简体中文](#中文)

By [@joshvlc](https://x.com/joshvlc) · [original post](https://x.com/joshvlc/status/2119894656221958575) · posted 2026-11-09

- **What it is:** A basketball arena game generated in a single shot.
- **Media:** Video, 19 s. About 109 views and 1 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 819 characters it is excerpted below, with our outline of how the brief is built.

**Prompt (excerpt; full text at the [source](https://x.com/joshvlc/status/2119894940595695756))**

```text
Can you make a 3D basketball game using THREE.js? It should have a player in two different colored uniforms for the two teams and should follow the basic rules of basketball. It should have basic funcionality:
- dribble (happens automatically when player runs)
[…]
```

**How the brief is built (our outline)**

- Asks for a 3D basketball game in THREE.js with two teams in different uniform colours, following the basic rules.
- Lists the controls one per line: automatic dribbling, hold to shoot, automatic dunks near the rim, jump or block without the ball, steal and pass.
- Defines single-player behaviour: CPU teammates who get open, the player always controlling whoever has the ball, and a CPU-controlled opponent.
- Adds fouls with free throws and a tip-off to start the game.
- Ends with sound effects and crowd cheering, and notes that Blender is installed if it wants it for the graphics.

To make one like it: the [Three.js starter](../../starter/threejs) turns a page with renderAt(t) into an MP4 (tested), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**一次生成的篮球馆游戏**

作者：[@joshvlc](https://x.com/joshvlc) · [原帖](https://x.com/joshvlc/status/2119894656221958575) · 发布于 2026-11-09

- **作品：** 一次生成的篮球馆游戏。
- **媒体：** 视频 19 秒。截至 2026-11-11 约 109 浏览、1 赞。
- **提示词：** 作者公开了原文，全文 819 个字符，上方只放节选，下面是我们整理的结构说明。

**这份提示词的结构（我们整理）**

- 要一个 THREE.js 写的 3D 篮球游戏，两队穿不同颜色球衣，遵守基本规则。
- 操作一行一条列出来：跑动时自动运球、按住投篮、篮下自动扣篮、没球时起跳封盖、抢断、传球。
- 规定单人模式的逻辑：队友由电脑控制并会主动跑空位，玩家始终控制持球人，对手全由电脑控制。
- 还要有犯规和罚球，比赛从跳球开始。
- 最后要音效和观众欢呼，并说明机器上装了 Blender，需要时可以拿来做画面。

想做类似的：[Three.js 起步脚本](../../starter/threejs)把带 renderAt(t) 的网页逐帧转成 MP4（实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Full Minecraft clone running in the browser](077-full-minecraft-clone-running-in-the-browser.md) · [All 145 cases](../../README.md) · [Reverse Scooby-Doo mystery game](079-reverse-scooby-doo-mystery-game.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
