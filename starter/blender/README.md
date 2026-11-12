# Blender starter: a scene built and rendered from Python

[简体中文](#中文)

Written and run by [apimodels.app](https://apimodels.app), not by the creators in this collection. `scene.py` builds a small animated scene (ground, a bouncing ball with squash and stretch, a sun, a camera) entirely in Python and renders it, which is the same loop the Blender cases here run at a much larger scale: Claude Fable 5.2 writes the script, Blender renders it headless, and the model looks at the frames before the final render.

```bash
blender -b -P scene.py -- --preview   # 3 key frames at 25% size, as PNG, in ./out
blender -b -P scene.py -- --final     # all 72 frames at 1280x720, as an H.264 MP4, in ./out
```

Measured on Blender 5.3.0 with EEVEE on an Apple M4: `--preview` took about 26 s and `--final` 77 s for the 3-second, 72-frame clip.

![Frame 18 of the preview render](preview_018.png)

Blender 5 notes, so the script runs without deprecation warnings:

- The EEVEE engine name is `BLENDER_EEVEE`.
- For video output, set `image_settings.media_type = "VIDEO"` before setting `file_format = "FFMPEG"`.
- New materials and worlds already have node trees; `use_nodes` is deprecated and not needed.

To grow it with Claude Code, open the folder, run Claude Code on Fable 5.2 and ask for the change ("add a second ball that collides with the first", "switch to Cycles at 64 samples"). Ask it to run `--preview` and look at the PNGs before every `--final`. The full walkthrough, with prompt templates, is [Blender Python with Claude Code](https://apimodels.app/blender-python-claude-code).

## 中文

这套脚本是 [apimodels.app](https://apimodels.app) 自己写、自己跑过的，不是合集里作者的作品。`scene.py` 全程用 Python 搭一个小动画场景（地面、一个会挤压变形的弹跳球、太阳光、摄像机）并渲染出来。合集里的 Blender 案例走的是同一个循环，只是规模大得多：Claude Fable 5.2 写脚本，Blender 在后台渲染，模型先看帧再做最终渲染。

命令见上方代码块：`--preview` 出 3 张 25% 尺寸的预览 PNG，`--final` 出全部 72 帧 1280x720 的 H.264 MP4，都在 `./out` 里。

Apple M4、Blender 5.3.0、EEVEE 实测：`--preview` 约 26 秒，`--final` 77 秒（3 秒、72 帧）。

Blender 5 的新写法（照这样写不会报弃用警告）：渲染引擎名是 `BLENDER_EEVEE`；输出视频要先设 `image_settings.media_type = "VIDEO"` 再设 `file_format = "FFMPEG"`；新建的材质和世界自带节点树，`use_nodes` 已弃用，不用再写。

想用 Claude Code 往上加东西：在这个目录里启动接了 Fable 5.2 的 Claude Code，直接说要改什么（「再加一个球，和第一个相撞」「换成 Cycles，64 采样」），并让它每次 `--final` 之前先跑 `--preview` 看图。完整图文教程和提示词模板见[用 Claude Code 写 Blender Python](https://apimodels.app/zh/blender-python-claude-code)。
