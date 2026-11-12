# Daybreak Switch: a cozy room from night to morning

Claude Fable 5.2 case 41 of 145 · Three.js Scenes and Animation · [简体中文](#中文)

By [@vib3coded](https://x.com/vib3coded) · [original post](https://x.com/vib3coded/status/2119876781700505627) · posted 2026-11-09

- **What it is:** "Daybreak Switch": an addictive volume slider that hides a cozy little room going from night to daybreak. It took 10 minutes and $8.43.
- **Media:** Video, 12 s. About 94K views and 1,113 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 5,996 characters it is excerpted below, with our outline of how the brief is built.
- **Note:** Prompt transcribed from the awesome-fable5-2-videos repository; it comes from the author's reply 2119877121732419838.

**Prompt (excerpt; full text at the [source](https://x.com/i/status/2119877121732419838))**

```text
Make "Daybreak Switch", No. 062 in a series of web material studies: a night-to-morning toggle in its own original style, as a single self-contained page (no libraries; raw WebGL2 + Web Audio + a 2D pixel buffer). Editorial layout: a small "Material Studies / No.
[…]
```

**How the brief is built (our outline)**

- Uses the same build template as Deep Dive Switch (this is No. 062 in the same series): one self-contained page with raw WebGL2, Web Audio and a 2D pixel buffer, in an editorial layout with readouts.
- THE SWITCH keeps the jelly-glass knob shader and the spring physics, and adds that the room seen through the knob is always fully lit.
- THE ROOM lists a cosy pixel-art room object by object; LIGHT AND THE MORNING has the knob drag dawn across it, day on one side and night on the other, with a 4×4 Bayer-dithered edge.
- THE STORY, BY POSITION ties events to the knob: a tabby cat goes from asleep to dancing in sunglasses, and from about 08:24 on the wall clock a puppy knocks at the door until it is let in.
- SOUND specifies a 100 BPM loop in F with five layers by position, and describes the door knock down to its frequencies (a thump sagging from about 98 to 60 Hz) and how far the music ducks under each hit.

To make one like it: the [Three.js starter](../../starter/threejs) turns a page with renderAt(t) into an MP4 (tested), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**Daybreak Switch：从黑夜到天亮**

作者：[@vib3coded](https://x.com/vib3coded) · [原帖](https://x.com/vib3coded/status/2119876781700505627) · 发布于 2026-11-09

- **作品：** "Daybreak Switch"：一个让人上瘾的音量滑块，里面藏着从夜晚到天亮的温馨小房间，10 分钟、$8.43。
- **媒体：** 视频 12 秒。截至 2026-11-11 约 9.4 万 浏览、1,113 赞。
- **提示词：** 作者公开了原文，全文 5,996 个字符，上方只放节选，下面是我们整理的结构说明。
- **备注：** 提示词转录自 awesome-fable5-2-videos 仓库，出自作者回复 2119877121732419838。

**这份提示词的结构（我们整理）**

- 和 Deep Dive Switch 用同一套搭建模板（它是同系列第 062 号）：自包含单页、原生 WebGL2、Web Audio 和 2D 像素缓冲，杂志式排版加读数。
- THE SWITCH 段沿用果冻玻璃旋钮着色器和弹簧手感，并规定旋钮里看到的房间永远是亮的。
- THE ROOM 段逐件列出一个温馨的像素小房间；LIGHT AND THE MORNING 段让旋钮把黎明拖过房间，一边白天一边黑夜，交界用 4×4 Bayer 抖动。
- THE STORY, BY POSITION 段把剧情绑在旋钮位置上：橘猫从睡着一路到戴墨镜跳舞；墙上的钟走到约 08:24 起，门外的小狗开始敲门，直到被放进来。
- SOUND 段规定 100 BPM、F 调循环、5 层音乐随位置加入，敲门声细到频率（一声闷响从约 98 Hz 降到约 60 Hz）以及每次敲门时音乐压低多少。

想做类似的：[Three.js 起步脚本](../../starter/threejs)把带 renderAt(t) 的网页逐帧转成 MP4（实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Deep Dive Switch: an underwater world inside a slider](040-deep-dive-switch-an-underwater-world-inside-a-slider.md) · [All 145 cases](../../README.md) · [Paris in 1940, built in three.js from Higgsfield references](042-paris-in-1940-built-in-three-js-from-higgsfield-references.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
