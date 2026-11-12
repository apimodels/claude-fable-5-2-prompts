# Deep Dive Switch: an underwater world inside a slider

Claude Fable 5.2 case 40 of 145 · Three.js Scenes and Animation · [简体中文](#中文)

By [@N1njaCodex](https://x.com/N1njaCodex) · [original post](https://x.com/N1njaCodex/status/2119883560937001387) · posted 2026-11-09 · [watch it in the apimodels.app gallery](https://apimodels.app/claude-fable-5-2-prompts/threejs)

- **What it is:** "Deep Dive Switch": asked for a volume slider, it built a whole underwater world with sea turtles inside it, for $7.48.
- **Media:** Video, 10 s. About 3,992 views and 108 likes as of 11 November 2026.
- **Prompt:** published by the creator; at 6,073 characters it is excerpted below, with our outline of how the brief is built.

**Prompt (excerpt; full text at the [source](https://x.com/N1njaCodex/status/2119884222475522068))**

```text
Make "Deep Dive Switch", No. 063 in a series of web material studies: a depth switch that goes from light to dark, from the sea's surface to the floor of the abyss. Build it as one self-contained page with no libraries: raw WebGL2, Web Audio and a 2D pixel buffer.

PAGE
- Editorial layout:
[…]
```

**How the brief is built (our outline)**

- Frames the piece as No. 063 in a series of "web material studies", built as one self-contained page with no libraries: raw WebGL2, Web Audio and a 2D pixel buffer.
- PAGE sets an editorial layout with three readouts, page colours that follow the depth, and support for phone widths.
- THE SWITCH specifies a 176×50 pixel-art cross-section redrawn on the CPU every frame and shown with nearest sampling, a glass "bathysphere" knob drawn in a fragment shader (about 1.28× magnification, RGB split at the rim, Fresnel tint, two highlights), spring motion with squash and stretch, and keyboard and ARIA slider controls.
- THE SEA lists every sprite zone by zone, from a beach with a sandcastle down to the abyss, with creatures that react as the knob comes near.
- LIGHT AND THE DIVE describes Bayer-dithered daylight that falls off with depth and a searchlight that comes on below the shallows.
- SOUND specifies an 84 BPM four-bar loop in D minor on one lookahead clock, five layers that fade in by depth and a list of interaction sounds; READOUTS map depth from 0 to 6,000 m onto zones and music.

To make one like it: the [Three.js starter](../../starter/threejs) turns a page with renderAt(t) into an MP4 (tested), and our [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) has six brief templates.

## 中文

**Deep Dive Switch 海底滑块**

作者：[@N1njaCodex](https://x.com/N1njaCodex) · [原帖](https://x.com/N1njaCodex/status/2119883560937001387) · 发布于 2026-11-09 · [在 apimodels.app 案例库看成片](https://apimodels.app/zh/claude-fable-5-2-prompts/threejs)

- **作品：** "Deep Dive Switch"：要一个音量滑块，它在里面做了一整个带海龟的水下世界，花费 $7.48。
- **媒体：** 视频 10 秒。截至 2026-11-11 约 3,992 浏览、108 赞。
- **提示词：** 作者公开了原文，全文 6,073 个字符，上方只放节选，下面是我们整理的结构说明。

**这份提示词的结构（我们整理）**

- 把作品定位成「网页材质研究」系列第 063 号，做成一个不依赖任何库的自包含单页：原生 WebGL2、Web Audio 加一个 2D 像素缓冲。
- PAGE 段定版式：杂志式排版、三个读数、整页颜色随深度变化，手机宽度也要能用。
- THE SWITCH 段写开关：176×50 的像素画海洋剖面每帧在 CPU 上重绘、最近邻采样显示；旋钮是片元着色器画的玻璃潜水球（约 1.28 倍放大、边缘 RGB 分离、菲涅尔色、两处高光），弹簧跟手、挤压拉伸，支持键盘和 ARIA 滑块。
- THE SEA 段从有沙堡的海滩到深渊逐区列出每个精灵，旋钮靠近时生物会有反应。
- LIGHT AND THE DIVE 段写光：日光随深度衰减并做 Bayer 抖动，浅海以下打开探照灯。
- SOUND 段规定 84 BPM、D 小调四小节循环、同一个前瞻调度时钟，5 层音乐随深度淡入，并列出交互音效；READOUTS 把 0 到 6,000 米的深度对应到分区和音乐层。

想做类似的：[Three.js 起步脚本](../../starter/threejs)把带 renderAt(t) 的网页逐帧转成 MP4（实测）；我们的 [Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)里有 6 个现成模板。

---

← [Manhattan at night: Fable versus Opus on one prompt](039-manhattan-at-night-fable-versus-opus-on-one-prompt.md) · [All 145 cases](../../README.md) · [Daybreak Switch: a cozy room from night to morning](041-daybreak-switch-a-cozy-room-from-night-to-morning.md) →

Collected by [apimodels.app](https://apimodels.app), the API platform that maintains this repository. The work belongs to its creator; our write-up is [CC BY 4.0](../../LICENSE). Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2).
