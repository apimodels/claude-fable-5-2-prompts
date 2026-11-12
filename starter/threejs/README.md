# Three.js starter: from a page with renderAt(t) to an MP4

[简体中文](#中文)

Written and run by [apimodels.app](https://apimodels.app), not by the creators in this collection. Many cases here are a single HTML page that Claude Fable 5.2 wrote; the reliable way to turn one into a video is to make every frame a pure function of time and capture the frames one by one, instead of screen-recording a live animation.

- `scene.html` is a minimal three.js scene that exposes `window.renderAt(t)` and `window.DURATION`. Everything that moves is computed from `t`: no clock, no `Math.random`, no accumulated state. Open it normally for a live preview.
- `capture.mjs` opens the page with `?capture=1` in headless Chromium (SwiftShader, so no GPU is needed), calls `renderAt(i / fps)` for every frame and saves a PNG of the canvas.

```bash
pnpm add -D playwright                 # or: npm i -D playwright
pnpm exec playwright install chromium  # or: npx playwright install chromium
node capture.mjs scene.html frames 30
ffmpeg -framerate 30 -i frames/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 scene.mp4
```

On our machine the capture wrote 120 frames at 1280×720 in 6.5 s, and rendering frame 45 again out of order gave a byte-identical PNG, which is the point of `renderAt(t)`: any frame can be re-rendered on its own.

When you ask Fable 5.2 for a scene of your own, put the contract in the first line of the prompt: "one self-contained three.js page, N seconds at 1280x720 and 30 fps, deterministic, expose window.renderAt(t) and window.DURATION". The full walkthrough, with a Claude Code skill file and prompt templates, is [Three.js with Claude Code](https://apimodels.app/claude-code-threejs).

## 中文

这套脚本是 [apimodels.app](https://apimodels.app) 自己写、自己跑过的，不是合集里作者的作品。合集里很多案例就是 Claude Fable 5.2 写的一个 HTML 页面；要把它稳定地变成视频，办法是让每一帧都只由时间决定，再一帧一帧截下来，而不是录屏录一个实时动画。

- `scene.html`：一个最小的 three.js 场景，暴露 `window.renderAt(t)` 和 `window.DURATION`。所有运动都由 `t` 算出来：不用时钟、不用 `Math.random`、不累积状态。直接打开就是实时预览。
- `capture.mjs`：用无头 Chromium（走 SwiftShader，不需要显卡）以 `?capture=1` 打开页面，逐帧调用 `renderAt(i / fps)`，把画布存成 PNG。

命令见上方代码块。我们本机 6.5 秒截完 120 帧 1280×720；乱序重渲第 45 帧，得到的 PNG 和原来逐字节一致，这正是 `renderAt(t)` 的意义：任意一帧都能单独重渲。

让 Fable 5.2 做你自己的场景时，把约定写进提示词第一句：「one self-contained three.js page, N seconds at 1280x720 and 30 fps, deterministic, expose window.renderAt(t) and window.DURATION」。完整图文教程（含 Claude Code skill 文件和提示词模板）见[用 Claude Code 写 Three.js](https://apimodels.app/zh/claude-code-threejs)。
