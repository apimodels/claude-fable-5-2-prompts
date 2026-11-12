# Claude Fable 5.2 提示词与案例：145 个用代码做出来的作品

[English](README.md) · 简体中文

Claude Fable 5.2 发布第一周，大家在 X 上晒出了大量作品：Blender 动画、Three.js 场景、动效宣传片、游戏、打斗动画、音乐和油画，全都是模型写代码做出来的。这里收了 145 个，每个都署了作者、链到原帖；作者公开了提示词的一并收录，几千字符的超长提示词放节选和结构说明。

说明：这个合集由 [apimodels.app](https://apimodels.app) 整理，我在这个 API 平台工作。apimodels.app 是多模型 API 聚合平台：一个 key，用 Anthropic 和 OpenAI 两种兼容接口调用 Claude Fable 5.2 和另外 150 多个图像、视频、音频、语言模型。[starter/](starter) 里的两套起步脚本是我们自己写、自己跑过的；[cases/](cases) 里都是别人的作品，由我们整理介绍。

## 一段话说清楚

Claude Fable 5.2（模型 ID `claude-fable-5-2`，Anthropic 于 2026 年 11 月 9 日发布）是语言模型：输入文字和图片，输出文字，上下文 100 万 token，单次最多输出 12.8 万 token。它自己不会画像素、也不会出声音。下面每一支片子、每一个游戏、每一首曲子、每一幅画，都是它写的代码跑出来的：Blender Python、Three.js 和原生 WebGL、Canvas、Web Audio、numpy、LilyPond，再由 Claude Code 这类 agent 去运行、渲染，大多数最后用 FFmpeg 编码成视频。很多出圈作品只用了一两句提示词，但背后跑得很久：鹈鹕骑车那支写了约 4,800 行 Python，整个会话输出约 110 万 token；那个 FPS 小关卡按作者的说法跑了 8 小时、花了约 $550。这 145 个案例发布于 2026 年 11 月 4 日到 11 日；11 月 9 日之前的几条是作者标为「Fable 5.5」的预发布测试。其中 38 个作者公开了完整提示词（9 份超长的只放节选并附结构说明），20 个只有作者的一句需求原话，87 个没有公开；没公开的我们一律不替作者补写。在 apimodels.app 上，Fable 5.2 每百万输入 token $4.80、输出 $24，Anthropic 官方价是 $8 / $40。

## 目录

- [Blender 3D 动画](#blender-3d-动画)（21 个）
- [Three.js 场景与动画](#threejs-场景与动画)（24 个）
- [代码动效与宣传片](#代码动效与宣传片)（21 个）
- [模型自己做的游戏](#模型自己做的游戏)（19 个）
- [角色动作与打斗](#角色动作与打斗)（21 个）
- [代码作曲](#代码作曲)（18 个）
- [代码绘画](#代码绘画)（21 个）
- [先看这 10 个：浏览量最高](#先看这-10-个浏览量最高)
- [好提示词都做了什么](#好提示词都做了什么)
- [自己动手做一个](#自己动手做一个)
- [常见问题](#常见问题)
- [署名、版权与许可](#署名版权与许可)

每个案例在 [cases/](cases) 下有单独一页：作者、原帖、做了什么、提示词公开情况，公开了的附原文。浏览和点赞数截至 2026-11-11。全部数据另有一份 [data/cases.json](data/cases.json)，方便程序读取。

## 先看这 10 个：浏览量最高

1. [8 小时做出的 3A 写实风 FPS 关卡](cases/games/067-realistic-aaa-style-fps-level-built-over-8-hours.md#中文)，@felixrieseberg，约 390.3 万 浏览（完整原文）
2. [连续开发 7 天的开放世界游戏](cases/games/074-open-world-game-developed-over-7-straight-days.md#中文)，@mattshumer_，约 81.5 万 浏览（未公开）
3. [直播里一次生成的 Blender 短片](cases/blender/003-13-shot-blender-short-with-a-macbook-and-clawd-made-on-a.md#中文)，@rileybrown，约 81 万 浏览（未公开）
4. [70 万笔的写实油画](cases/painting/125-photoreal-oil-painting-in-700-000-strokes.md#中文)，@jkeatn，约 54.6 万 浏览（只有需求原话）
5. [小船穿越 8 个世界的游戏](cases/games/069-small-boat-sailing-through-8-worlds-with-a-fable-made.md#中文)，@kevin_t_ngo，约 46.2 万 浏览（未公开）
6. [先设定画家人格再作画](cases/painting/126-paintings-made-after-first-inventing-a-painter-persona.md#中文)，@jkeatn，约 43.6 万 浏览（未公开）
7. [Teto 的 Vocaloid 原创情歌](cases/music/109-original-vocaloid-love-song-featuring-teto.md#中文)，@peach2k2，约 38.6 万 浏览（只有需求原话）
8. [Blender 里的史前恐龙水潭](cases/blender/002-prehistoric-watering-hole-with-dinosaurs-built-in-blender.md#中文)，@jeremyberman，约 28.2 万 浏览（未公开）
9. [一次生成的代码绘画作品](cases/painting/141-code-painting-generated-in-a-single-pass.md#中文)，@devsvn2，约 25.4 万 浏览（未公开）
10. [哈利波特 × 堡垒之夜混搭游戏](cases/games/073-harry-potter-and-fortnite-mashup-game.md#中文)，@mattshumer_，约 16.9 万 浏览（完整原文）

## 好提示词都做了什么

下面这几条是从合集里 38 份公开提示词里总结的。

- **说清楚「做完」长什么样，然后给它时间。** 鹈鹕那条只有三句话，但写明了交付物（一个做好的视频文件）、标准（解剖结构可信、传动系统真能转、真实光照），还明确允许它慢慢做：「Take the time it needs」。
- **用数字定设计，别只用形容词。** 机车变形动画那份给了以米为单位的尺寸、把 120 帧的变形拆成 5 段各 24 帧、音乐定在 144 bpm；僵尸战鹰那份规定了面数上限、贴图尺寸和文件大小。有了数字，模型才有东西对照着检查。
- **让每一帧都是时间的函数。** 网页类作品，要求做成自包含单页并暴露 `window.renderAt(t)`（体素巴黎那份就是这么写的），无头浏览器就能按需截任意一帧，帧率稳定。Blender 里对应的做法是脚本按帧设定每个状态，机车那份管这叫「故事时钟」。
- **贵的那次渲染之前，先让它自己检查。** 写得最好的几份都以检查收尾：先渲 6 张关键帧自己看（僵尸手）、逐帧检查穿模和车轮打滑（机车动画）、看每个剪辑点前后两侧的静帧（机器人夜市）。Fable 5.2 能看图，所以自查靠静帧来做。
- **凡是花钱的步骤，前面都设暂停点和花费关卡。** 机器人夜市那份中途停两次等确认；僵尸手那份要求先报出云端 GPU 任务预计和最多花多少积分，等「同意」才开跑。合集里作者自述的花费，从 4K Blender 渲染租 GPU 的 $5.75，到 8 小时做游戏的约 $550。
- **题目开放时，给它一个理由或一个身份。** 合集里点赞最多的油画帖，是先让模型给自己设定一个画家人格再动笔（@jkeatn）；还有人让它画「做你自己是什么感觉」（@ZryMiller）。一句话也能出圈：「invent a new musical form」约 13.2 万浏览。
- **effort 档位要有意识地选。** 作者们用过 medium（开源项目预告片）、High（灯塔场景）和 Extra High（LilyPond 写巴赫众赞歌）。按 Anthropic 发布公告，API 默认 high，Claude Code 和 Claude 应用默认 medium。

## Blender 3D 动画

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 1 | [写实 3D 鹈鹕骑自行车短片](cases/blender/001-photoreal-3d-pelican-riding-a-bicycle-driven-from-claude.md#中文) | [@techfren](https://x.com/techfren) | 完整原文 | 16.3 万 |
| 2 | [Blender 里的史前恐龙水潭](cases/blender/002-prehistoric-watering-hole-with-dinosaurs-built-in-blender.md#中文) | [@jeremyberman](https://x.com/jeremyberman) | 未公开 | 28.2 万 |
| 3 | [直播里一次生成的 Blender 短片](cases/blender/003-13-shot-blender-short-with-a-macbook-and-clawd-made-on-a.md#中文) | [@rileybrown](https://x.com/rileybrown) | 未公开 | 81 万 |
| 4 | [蒸汽机车变形成机器人的 2D 动画短片](cases/blender/004-steam-locomotive-transforms-into-a-robot-in-a-2d-anime-short.md#中文) | [@0kncn](https://x.com/0kncn) | 节选 + 结构说明 | 6.9 万 |
| 5 | [Blender MCP 做的游戏级僵尸战鹰](cases/blender/005-game-ready-3d-zombie-war-eagle-built-through-blender-mcp.md#中文) | [@maxt3chno](https://x.com/maxt3chno) | 节选 + 结构说明 | 2.1 万 |
| 6 | [Blender 重建耶稣最后一周的耶路撒冷](cases/blender/006-jerusalem-in-the-final-week-of-jesus-s-life-rebuilt-in.md#中文) | [@kplikethebird](https://x.com/kplikethebird) | 完整原文 | 1 万 |
| 7 | [布加迪 Tourbillon 写实 3D 渲染](cases/blender/007-photoreal-bugatti-tourbillon-render-from-one-prompt-and-a.md#中文) | [@xikhar](https://x.com/xikhar) | 未公开 | 11.2 万 |
| 8 | [星战 Blender Bench：吉奥诺西斯战役](cases/blender/008-star-wars-blender-bench-the-first-battle-of-geonosis.md#中文) | [@adityavg13](https://x.com/adityavg13) | 未公开 | 4.4 万 |
| 9 | [会爬行和后空翻的僵尸手动画](cases/blender/009-rigged-cartoon-zombie-hand-that-crawls-and-does-a-backflip.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 节选 + 结构说明 | 6.3 万 |
| 10 | [会变形的汽车人卡车及变形动画](cases/blender/010-transformer-truck-with-an-animation-of-it-transforming.md#中文) | [@camperaigg](https://x.com/camperaigg) | 完整原文 | 3,471 |
| 11 | [哈尔的移动城堡及内部机械](cases/blender/011-howl-s-moving-castle-with-its-internal-machinery-shown.md#中文) | [@camperaigg](https://x.com/camperaigg) | 完整原文 | 3,019 |
| 12 | [Blender 里做的机械心脏](cases/blender/012-mechanical-heart-with-its-inner-workings-revealed-in-blender.md#中文) | [@camperaigg](https://x.com/camperaigg) | 完整原文 | 5,836 |
| 13 | [日本创作者的 Blender 3D 动画测试](cases/blender/013-blender-3d-animation-test-from-a-japanese-creator.md#中文) | [@ICO_AIvideo](https://x.com/ICO_AIvideo) | 未公开 | 10.4 万 |
| 14 | [零人工反馈完成的 Blender 短片](cases/blender/014-blender-short-finished-with-zero-human-feedback.md#中文) | [@HyunSeob_](https://x.com/HyunSeob_) | 未公开 | 583 |
| 15 | [让 Fable 自编故事的 4K 短片](cases/blender/015-story-of-fable-s-own-invention-told-as-an-18-shot-4k-short.md#中文) | [@CalebJones800](https://x.com/CalebJones800) | 只有需求原话 | 113 |
| 16 | [千灯神殿：与 Opus 同题对比](cases/blender/016-temple-of-a-thousand-lamps-compared-with-opus-on-the-same.md#中文) | [@akshar_ai](https://x.com/akshar_ai) | 未公开 | 1,498 |
| 17 | [4 张 Airbnb 截图重建的 3D 房屋漫游](cases/blender/017-airbnb-house-rebuilt-as-a-3d-walkthrough-from-4-screenshots.md#中文) | [@WalidBou07](https://x.com/WalidBou07) | 完整原文 | 131 |
| 18 | [四季轮换的玻璃屋 Blender 动画](cases/blender/018-glass-house-through-the-four-seasons-animated-in-blender.md#中文) | [@lynzhong_growth](https://x.com/lynzhong_growth) | 未公开 | 5,214 |
| 19 | [Blender 里的万年历时钟机械动画](cases/blender/019-perpetual-calendar-clock-mechanism-animated-in-blender.md#中文) | [@MakeAI_CEO](https://x.com/MakeAI_CEO) | 未公开 | 2,486 |
| 20 | [Blender MCP 做的低多边形浮岛](cases/blender/020-low-poly-floating-island-scene-made-with-blender-mcp.md#中文) | [@rewind02](https://x.com/rewind02) | 完整原文 | 923 |
| 21 | [1,110 行代码的 Blender 短片](cases/blender/021-blender-short-from-1-110-lines-of-python-in-16-4-minutes.md#中文) | [@FreshOutofBeta](https://x.com/FreshOutofBeta) | 未公开 | 63 |

## Three.js 场景与动画

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 22 | [three.js 机甲弓箭手一箭射穿大海](cases/threejs/022-mech-archer-firing-an-arrow-through-the-ocean.md#中文) | [@camperaigg](https://x.com/camperaigg) | 只有需求原话 | 1,111 |
| 23 | [three.js 带你掉进黑洞](cases/threejs/023-falling-into-a-black-hole-in-three-js.md#中文) | [@camperaigg](https://x.com/camperaigg) | 只有需求原话 | 1.3 万 |
| 24 | [three.js 划火柴特写](cases/threejs/024-match-strike-in-slow-motion-built-in-three-js.md#中文) | [@camperaigg](https://x.com/camperaigg) | 只有需求原话 | 1.6 万 |
| 25 | [three.js 写的 31 米巨浪](cases/threejs/025-rowing-into-a-31-m-wave-in-three-js.md#中文) | [@camperaigg](https://x.com/camperaigg) | 只有需求原话 | 1.9 万 |
| 26 | [three.js 闪电：从云层劈到地面](cases/threejs/026-riding-a-lightning-bolt-from-cloud-to-ground.md#中文) | [@camperaigg](https://x.com/camperaigg) | 只有需求原话 | 10.6 万 |
| 27 | [83 秒 three.js 逐帧动画短片](cases/threejs/027-83-second-animated-short-rendered-frame-by-frame-in-three-js.md#中文) | [@noisyb0y1](https://x.com/noisyb0y1) | 未公开 | 1.2 万 |
| 28 | [体素风巴黎 14 秒 three.js 动画](cases/threejs/028-voxel-paris-as-a-14-second-three-js-animation.md#中文) | [@RezAIT00](https://x.com/RezAIT00) | 节选 + 结构说明 | 4,436 |
| 29 | [73 秒机器人夜市短片](cases/threejs/029-robot-night-market-short-film-with-procedural-sound.md#中文) | [@evaninfra](https://x.com/evaninfra) | 节选 + 结构说明 | 53 |
| 30 | [巨石阵冬至日出 three.js 交互场景](cases/threejs/030-interactive-stonehenge-winter-solstice-sunrise-in-three-js.md#中文) | [@MeltTheManual](https://x.com/MeltTheManual) | 未公开 | 153 |
| 31 | [ASML EUV 光刻机原理可视化](cases/threejs/031-how-an-asml-euv-lithography-machine-works-in-three-js.md#中文) | [@miki_code](https://x.com/miki_code) | 未公开 | 182 |
| 32 | [three.js 喷气发动机剖面动画](cases/threejs/032-cutaway-animation-of-a-jet-engine-in-three-js.md#中文) | [@renoiseai](https://x.com/renoiseai) | 未公开 | 820 |
| 33 | [32 万粒子的 three.js 特效](cases/threejs/033-particle-effect-with-320-000-particles-in-three-js.md#中文) | [@mdjunaidap](https://x.com/mdjunaidap) | 未公开 | 1,216 |
| 34 | [three.js 火星车场景](cases/threejs/034-mars-rover-scene-in-three-js.md#中文) | [@koss_ai](https://x.com/koss_ai) | 未公开 | 244 |
| 35 | [水豚主题 three.js 动画](cases/threejs/035-capybara-themed-animation-built-in-three-js.md#中文) | [@anstapnever](https://x.com/anstapnever) | 未公开 | 246 |
| 36 | [4 Elements：多模型同题做水火风土](cases/threejs/036-4-elements-water-fire-wind-and-earth-from-each-model.md#中文) | [@orcdev](https://x.com/orcdev) | 未公开 | 3,592 |
| 37 | [复刻《老友记》Monica 的公寓](cases/threejs/037-monica-s-apartment-from-friends-rebuilt-in-three-js.md#中文) | [@chetaslua](https://x.com/chetaslua) | 未公开 | 1.3 万 |
| 38 | [冰之大教堂：与 Opus 同题对比](cases/threejs/038-cathedral-of-ice-run-head-to-head-with-opus.md#中文) | [@QQTeng](https://x.com/QQTeng) | 只有需求原话 | 7.6 万 |
| 39 | [夜晚的曼哈顿：Fable 与 Opus 同题对比](cases/threejs/039-manhattan-at-night-fable-versus-opus-on-one-prompt.md#中文) | [@KernelChai](https://x.com/KernelChai) | 只有需求原话 | 629 |
| 40 | [Deep Dive Switch 海底滑块](cases/threejs/040-deep-dive-switch-an-underwater-world-inside-a-slider.md#中文) | [@N1njaCodex](https://x.com/N1njaCodex) | 节选 + 结构说明 | 3,992 |
| 41 | [Daybreak Switch：从黑夜到天亮](cases/threejs/041-daybreak-switch-a-cozy-room-from-night-to-morning.md#中文) | [@vib3coded](https://x.com/vib3coded) | 节选 + 结构说明 | 9.4 万 |
| 42 | [three.js 还原 1940 年的巴黎](cases/threejs/042-paris-in-1940-built-in-three-js-from-higgsfield-references.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 未公开 | 1.5 万 |
| 43 | [High 档的风暴灯塔场景](cases/threejs/043-lighthouse-in-a-storm-at-high-effort.md#中文) | [@rohit3a](https://x.com/rohit3a) | 未公开 | 1,857 |
| 44 | [作者自写提示词的写实灯塔场景](cases/threejs/044-photoreal-lighthouse-scene-from-the-author-s-own-prompt.md#中文) | [@viewsfrom02108](https://x.com/viewsfrom02108) | 未公开 | 304 |
| 45 | [Discovery：101 秒短片](cases/threejs/045-discovery-a-101-second-short-film-in-three-js.md#中文) | [@YinYangYoeshi](https://x.com/YinYangYoeshi) | 未公开 | 449 |

## 代码动效与宣传片

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 46 | [ChatGPT 四周年致敬动效片](cases/motion-graphics/046-motion-graphics-tribute-to-chatgpt-s-fourth-anniversary.md#中文) | [@Khazix0918](https://x.com/Khazix0918) | 完整原文 | 9.1 万 |
| 47 | [30 秒动态图形简历作品集](cases/motion-graphics/047-30-second-motion-graphics-portfolio-piece-for-a-resume.md#中文) | [@Leviwoyun](https://x.com/Leviwoyun) | 完整原文 | 2.4 万 |
| 48 | [15 秒动效 showreel](cases/motion-graphics/048-15-second-motion-designer-showreel.md#中文) | [@himanshutwtxs](https://x.com/himanshutwtxs) | 完整原文 | 1,215 |
| 49 | [最惊艳动效片，含 4 万只鸟群模拟](cases/motion-graphics/049-most-impressive-motion-design-video-with-a-40-000-bird-flock.md#中文) | [@techfren](https://x.com/techfren) | 只有需求原话 | 1,002 |
| 50 | [讲解 LLM 工作原理的 mograph 动画](cases/motion-graphics/050-mograph-animation-explaining-how-llms-work.md#中文) | [@MatthewBerman](https://x.com/MatthewBerman) | 只有需求原话 | 7,594 |
| 51 | [Clawd 小人制作并发布 Fable 5.2](cases/motion-graphics/051-clawd-building-and-releasing-claude-fable-5-2-animated.md#中文) | [@other__reality](https://x.com/other__reality) | 完整原文 | 1.3 万 |
| 52 | [90 秒 Fable 5.2 自我宣传片](cases/motion-graphics/052-90-second-fable-5-2-self-promotion-video.md#中文) | [@yasu_919](https://x.com/yasu_919) | 完整原文 | 189 |
| 53 | [API 网站的产品发布视频](cases/motion-graphics/053-product-launch-video-for-an-api-website.md#中文) | [@PeetuKupiainen](https://x.com/PeetuKupiainen) | 完整原文 | 242 |
| 54 | [写实延时摄影风的写作历史短片](cases/motion-graphics/054-the-history-of-writing-a-photoreal-historical-time-lapse.md#中文) | [@rileybrown](https://x.com/rileybrown) | 节选 + 结构说明 | 4.7 万 |
| 55 | [日文解说视频：Fable 5.2 有多强](cases/motion-graphics/055-japanese-explainer-on-just-how-capable-fable-5-2-is.md#中文) | [@tankazunori0914](https://x.com/tankazunori0914) | 完整原文 | 1,131 |
| 56 | [日文 Fable 5.2 最强实力宣传片](cases/motion-graphics/056-japanese-showcase-video-of-fable-5-2-at-full-strength.md#中文) | [@marcy_sns](https://x.com/marcy_sns) | 完整原文 | 983 |
| 57 | [告别 Opus 5.5 的 15 秒动画](cases/motion-graphics/057-15-second-farewell-to-opus-5-5-as-fable-5-2-arrives.md#中文) | [@kaif9998](https://x.com/kaif9998) | 完整原文 | 1,588 |
| 58 | [发布日拿来分享的最惊艳动画](cases/motion-graphics/058-launch-day-animation-built-to-be-shared.md#中文) | [@ici_dab](https://x.com/ici_dab) | 完整原文 | 89 |
| 59 | [用子 agent 做的 60 秒发布动画](cases/motion-graphics/059-60-second-fable-5-2-launch-film-made-with-opus-5-5-subagents.md#中文) | [@grafikcem](https://x.com/grafikcem) | 完整原文 | 185 |
| 60 | [只用代码给自己做的发布视频](cases/motion-graphics/060-its-own-launch-video-made-with-code-only.md#中文) | [@furkancavlakcom](https://x.com/furkancavlakcom) | 完整原文 | 3.6 万 |
| 61 | [开源项目的社交媒体动画预告片](cases/motion-graphics/061-animated-social-media-trailer-for-an-open-source-project.md#中文) | [@midudev](https://x.com/midudev) | 完整原文 | 9.7 万 |
| 62 | [走进灯塔的 2D 夜景动画](cases/motion-graphics/062-2d-night-time-animation-of-a-man-entering-a-lighthouse.md#中文) | [@talhaXclusively](https://x.com/talhaXclusively) | 完整原文 | 48 |
| 63 | [一次完成的 9:16 竖版剪辑](cases/motion-graphics/063-one-pass-9-16-vertical-edit-with-animations-and-mographs.md#中文) | [@The_Alex](https://x.com/The_Alex) | 只有需求原话 | 3,945 |
| 64 | [Convex 产品讲解动画](cases/motion-graphics/064-animated-product-explainer-for-convex.md#中文) | [@Rasmic](https://x.com/Rasmic) | 未公开 | 1.2 万 |
| 65 | [用 Fable 5.2 做的发布宣传片](cases/motion-graphics/065-launch-promotional-video-made-with-fable-5-2.md#中文) | [@DoctorYev](https://x.com/DoctorYev) | 未公开 | 1,630 |
| 66 | [AI 2027 文档的动画解说](cases/motion-graphics/066-animated-explainer-of-the-ai-2027-document.md#中文) | [@Btheriot](https://x.com/Btheriot) | 未公开 | 51 |

## 模型自己做的游戏

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 67 | [8 小时做出的 3A 写实风 FPS 关卡](cases/games/067-realistic-aaa-style-fps-level-built-over-8-hours.md#中文) | [@felixrieseberg](https://x.com/felixrieseberg) | 完整原文 | 390.3 万 |
| 68 | [three.js 写的 FPS 游戏](cases/games/068-first-person-shooter-written-in-three-js.md#中文) | [@JaydenDavisNC](https://x.com/JaydenDavisNC) | 未公开 | 4.3 万 |
| 69 | [小船穿越 8 个世界的游戏](cases/games/069-small-boat-sailing-through-8-worlds-with-a-fable-made.md#中文) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | 未公开 | 46.2 万 |
| 70 | [游戏《Gilt & Gutter》](cases/games/070-gilt-gutter-a-game-built-with-fable.md#中文) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | 未公开 | 10.1 万 |
| 71 | [4 小时做出的 3A 质感游戏](cases/games/071-game-with-an-aaa-quality-look-made-in-4-hours.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 未公开 | 1.9 万 |
| 72 | [Unreal 里做的《战争机器》风格游戏](cases/games/072-gears-of-war-style-game-built-in-unreal.md#中文) | [@MatthewBerman](https://x.com/MatthewBerman) | 未公开 | 14 万 |
| 73 | [哈利波特 × 堡垒之夜混搭游戏](cases/games/073-harry-potter-and-fortnite-mashup-game.md#中文) | [@mattshumer_](https://x.com/mattshumer_) | 完整原文 | 16.9 万 |
| 74 | [连续开发 7 天的开放世界游戏](cases/games/074-open-world-game-developed-over-7-straight-days.md#中文) | [@mattshumer_](https://x.com/mattshumer_) | 未公开 | 81.5 万 |
| 75 | [飞越里斯本的休闲飞行游戏](cases/games/075-casual-flying-game-over-lisbon-playable-online.md#中文) | [@goncalo_canhoto](https://x.com/goncalo_canhoto) | 未公开 | 1.2 万 |
| 76 | [150 万笔刷的手绘油画风游戏](cases/games/076-hand-painted-oil-paint-game-with-1-5-million-brush-strokes.md#中文) | [@BlendiByl](https://x.com/BlendiByl) | 未公开 | 16.2 万 |
| 77 | [浏览器里的完整 Minecraft 克隆](cases/games/077-full-minecraft-clone-running-in-the-browser.md#中文) | [@intheworldofai](https://x.com/intheworldofai) | 完整原文 | 6,829 |
| 78 | [一次生成的篮球馆游戏](cases/games/078-one-shot-3d-basketball-arena-game-in-three-js.md#中文) | [@joshvlc](https://x.com/joshvlc) | 节选 + 结构说明 | 109 |
| 79 | [反向史酷比推理游戏](cases/games/079-reverse-scooby-doo-mystery-game.md#中文) | [@emollick](https://x.com/emollick) | 未公开 | 3.2 万 |
| 80 | [一款卡丁车竞速游戏](cases/games/080-go-kart-racing-game-built-with-fable-5-2.md#中文) | [@petergyang](https://x.com/petergyang) | 未公开 | 3.2 万 |
| 81 | [糖豆人（Fall Guys）风格游戏](cases/games/081-game-in-the-style-of-fall-guys.md#中文) | [@alexmichael](https://x.com/alexmichael) | 未公开 | 2,030 |
| 82 | [Roblox 恐怖游戏](cases/games/082-horror-game-made-in-roblox.md#中文) | [@mihawkxxxxx](https://x.com/mihawkxxxxx) | 未公开 | 1,150 |
| 83 | [开源的炼金术游戏](cases/games/083-open-source-alchemy-game-on-github.md#中文) | [@winchxyz](https://x.com/winchxyz) | 未公开 | 442 |
| 84 | [一款奇幻风格游戏](cases/games/084-fantasy-game-built-with-fable-5-2.md#中文) | [@flxrnc](https://x.com/flxrnc) | 未公开 | 646 |
| 85 | [可玩的鹈鹕骑自行车小游戏](cases/games/085-playable-pelican-on-a-bicycle-mini-game.md#中文) | [@siennatries](https://x.com/siennatries) | 未公开 | 71 |

## 角色动作与打斗

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 86 | [火柴人慢动作打斗，对比 Opus 成本](cases/character-action/086-stick-figure-fight-with-slow-motion-and-an-opus-cost.md#中文) | [@DanielZambrini](https://x.com/DanielZambrini) | 未公开 | 3.3 万 |
| 87 | [火柴人打斗对比 Gemini 4 Carbon](cases/character-action/087-the-same-stick-figure-fight-test-gemini-4-carbon-vs-fable-5.md#中文) | [@DanielZambrini](https://x.com/DanielZambrini) | 未公开 | 2.1 万 |
| 88 | [火柴人打斗，对比 Fable 5.5 灰度版](cases/character-action/088-stick-figure-fight-animation-compared-with-an-earlier-fable.md#中文) | [@leo114119](https://x.com/leo114119) | 未公开 | 1,384 |
| 89 | [号称电影级的火柴人打斗与特效](cases/character-action/089-stick-figure-fight-billed-as-cinematic-with-effects.md#中文) | [@RJasonHA](https://x.com/RJasonHA) | 未公开 | 635 |
| 90 | [15 秒火柴人光剑对决，对比 Opus 5.5](cases/character-action/090-15-second-stick-figure-lightsaber-duel-compared-with-opus-5.md#中文) | [@jiangjiangling](https://x.com/jiangjiangling) | 未公开 | 383 |
| 91 | [Blender 里复刻《暗黑破坏神 IV》](cases/character-action/091-diablo-iv-recreation-in-blender-with-a-rigged-fighting.md#中文) | [@ChengYi3629](https://x.com/ChengYi3629) | 未公开 | 320 |
| 92 | [魂系 Boss 战，附在线版](cases/character-action/092-soulslike-boss-fight-with-an-online-version.md#中文) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | 未公开 | 10.1 万 |
| 93 | [“铁竹”Boss 战，3,400 行 three.js](cases/character-action/093-iron-bamboo-boss-fight-in-3-400-lines-of-three-js.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 未公开 | 1.4 万 |
| 94 | [一条提示词做出的 three.js 剑斗游戏](cases/character-action/094-full-three-js-sword-fighting-game-from-a-single-prompt.md#中文) | [@FutureFlynn5](https://x.com/FutureFlynn5) | 未公开 | 40 |
| 95 | [格斗游戏 Courtyard Kings](cases/character-action/095-courtyard-kings-a-fighting-game-with-audio-from-elevenlabs.md#中文) | [@promodenstudio](https://x.com/promodenstudio) | 未公开 | 174 |
| 96 | [36 分钟把 Tripo 模型做成绑定角色](cases/character-action/096-raw-tripo-model-turned-into-a-rigged-game-character-in.md#中文) | [@0xKense1](https://x.com/0xKense1) | 未公开 | 4.8 万 |
| 97 | [不到 3 小时做出的武装动作角色](cases/character-action/097-armed-and-armored-action-character-made-with-tripo-and.md#中文) | [@luccacerf](https://x.com/luccacerf) | 未公开 | 1.6 万 |
| 98 | [为卡通 FPS 从零设计新敌人](cases/character-action/098-new-enemy-designed-from-scratch-for-a-cartoon-fps.md#中文) | [@whaledevstudios](https://x.com/whaledevstudios) | 只有需求原话 | 1,231 |
| 99 | [摄像头追踪双手的 AR 拳击游戏](cases/character-action/099-ar-boxing-game-with-camera-hand-tracking.md#中文) | [@TusharXo](https://x.com/TusharXo) | 未公开 | 334 |
| 100 | [《影之刃零》风格的 3D 动作游戏](cases/character-action/100-3d-action-game-in-the-style-of-shadow-blade-zero.md#中文) | [@ohmygameai](https://x.com/ohmygameai) | 未公开 | 754 |
| 101 | [从参考视频生成的 3D 动作动画](cases/character-action/101-3d-action-animation-generated-from-a-reference-video.md#中文) | [@KHvostikk](https://x.com/KHvostikk) | 未公开 | 6.3 万 |
| 102 | [用球和圆锥拼出的“功夫喵”](cases/character-action/102-kung-fu-cat-built-in-code-from-spheres-and-cones.md#中文) | [@New202064737](https://x.com/New202064737) | 未公开 | 79 |
| 103 | [High 档一条提示词做的动作作品](cases/character-action/103-one-prompt-action-piece-on-fable-5-2-at-high-effort.md#中文) | [@tymarsha](https://x.com/tymarsha) | 未公开 | 265 |
| 104 | [一次生成的《街头霸王 2》克隆](cases/character-action/104-street-fighter-2-clone-generated-in-one-go.md#中文) | [@BertrandDiouly](https://x.com/BertrandDiouly) | 未公开 | 558 |
| 105 | [用 Spawn 一次生成的动作游戏](cases/character-action/105-action-game-generated-in-a-single-run-on-spawn.md#中文) | [@OneHitKillDev](https://x.com/OneHitKillDev) | 未公开 | 1,508 |
| 106 | [守望先锋式第三人称 PvPvE 英雄乱斗](cases/character-action/106-overwatch-style-third-person-pvpve-hero-brawler.md#中文) | [@Pumpnasterr](https://x.com/Pumpnasterr) | 未公开 | 1,785 |

## 代码作曲

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 107 | [原创交响乐加配套视频](cases/music/107-original-symphony-with-a-matching-video.md#中文) | [@imjustnewatai](https://x.com/imjustnewatai) | 只有需求原话 | 14.2 万 |
| 108 | [发明一种新的音乐形式](cases/music/108-inventing-a-new-musical-form.md#中文) | [@imjustnewatai](https://x.com/imjustnewatai) | 只有需求原话 | 13.2 万 |
| 109 | [Teto 的 Vocaloid 原创情歌](cases/music/109-original-vocaloid-love-song-featuring-teto.md#中文) | [@peach2k2](https://x.com/peach2k2) | 只有需求原话 | 38.6 万 |
| 110 | [用 LilyPond 写巴赫风四声部众赞歌](cases/music/110-bach-style-4-part-chorale-written-in-lilypond.md#中文) | [@aug5thmusic](https://x.com/aug5thmusic) | 完整原文 | 6.7 万 |
| 111 | [试用期里精心写提示词的作曲](cases/music/111-composition-from-a-carefully-written-prompt-during-the-trial.md#中文) | [@GrayCan1392](https://x.com/GrayCan1392) | 未公开 | 145 |
| 112 | [Python 同时写出画和音乐](cases/music/112-painting-and-music-generated-together-in-python.md#中文) | [@wquguru](https://x.com/wquguru) | 未公开 | 3,425 |
| 113 | [一首 acid techno 曲目](cases/music/113-acid-techno-track-made-with-fable.md#中文) | [@Masimo_Blue](https://x.com/Masimo_Blue) | 未公开 | 2,407 |
| 114 | [用 CC0 采样编排的小船游戏预告配乐](cases/music/114-trailer-score-for-a-small-boat-game-from-cc0-samples.md#中文) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | 未公开 | 2,776 |
| 115 | [代码作曲，附创作过程记录](cases/music/115-music-composed-in-code-with-a-write-up-of-the-process.md#中文) | [@taka_claudecode](https://x.com/taka_claudecode) | 未公开 | 38 |
| 116 | [大制作风格解说片：点一个链接时发生了什么](cases/music/116-big-studio-explainer-on-what-happens-when-you-click-a-link.md#中文) | [@MojojojoHojo](https://x.com/MojojojoHojo) | 只有需求原话 | 57 |
| 117 | [把一篇离谱的真实论文用代码复现成短视频](cases/music/117-outlandish-real-research-paper-recreated-as-a-short-video.md#中文) | [@ronginooth](https://x.com/ronginooth) | 完整原文 | 102 |
| 118 | [Web Audio 黑胶唱机](cases/music/118-web-audio-turntable-with-visuals-and-sound.md#中文) | [@JuanDHernandezG](https://x.com/JuanDHernandezG) | 未公开 | 30 |
| 119 | [自选工具做出的 Web Audio 钟声](cases/music/119-left-to-choose-its-own-tools-it-built-web-audio-bells.md#中文) | [@Maaaaaaadiii](https://x.com/Maaaaaaadiii) | 只有需求原话 | 169 |
| 120 | [Higgsfield 的共振峰合成器](cases/music/120-formant-synthesizer-from-higgsfield.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 未公开 | 1.2 万 |
| 121 | [让 Fable 用代码唱歌](cases/music/121-getting-fable-to-sing-through-code.md#中文) | [@higgsfield_ai](https://x.com/higgsfield_ai) | 未公开 | 1.3 万 |
| 122 | [Blender 加 Reaper 声音设计](cases/music/122-sound-design-in-blender-and-reaper-from-iphone-recordings.md#中文) | [@AmirMushich](https://x.com/AmirMushich) | 未公开 | 7.7 万 |
| 123 | [前电影配乐师的氛围音乐工作站](cases/music/123-former-film-composer-s-ambient-music-workstation-with-a-co.md#中文) | [@FinanceYF5](https://x.com/FinanceYF5) | 未公开 | 1,361 |
| 124 | [带歌词的音乐 MV](cases/music/124-music-video-for-a-song-with-lyrics.md#中文) | [@WesRoth](https://x.com/WesRoth) | 未公开 | 8,415 |

## 代码绘画

| # | 案例 | 作者 | 提示词 | 浏览 |
| --- | --- | --- | --- | --- |
| 125 | [70 万笔的写实油画](cases/painting/125-photoreal-oil-painting-in-700-000-strokes.md#中文) | [@jkeatn](https://x.com/jkeatn) | 只有需求原话 | 54.6 万 |
| 126 | [先设定画家人格再作画](cases/painting/126-paintings-made-after-first-inventing-a-painter-persona.md#中文) | [@jkeatn](https://x.com/jkeatn) | 未公开 | 43.6 万 |
| 127 | [人格系列：画家 Dermot Hale](cases/painting/127-persona-series-works-by-the-painter-dermot-hale.md#中文) | [@jkeatn](https://x.com/jkeatn) | 未公开 | 5.2 万 |
| 128 | [人格系列：Tidewright](cases/painting/128-persona-series-the-tidewright-paintings.md#中文) | [@jkeatn](https://x.com/jkeatn) | 未公开 | 4.9 万 |
| 129 | [710,989 笔的海浪油画](cases/painting/129-ocean-wave-oil-painting-in-710-989-strokes.md#中文) | [@hoppycat](https://x.com/hoppycat) | 未公开 | 535 |
| 130 | [代码画作《Cheek to Cheek》](cases/painting/130-cheek-to-cheek-a-painting-in-801-582-strokes.md#中文) | [@hoppycat](https://x.com/hoppycat) | 未公开 | 376 |
| 131 | [MS Paint 克隆里的 11,066 笔](cases/painting/131-masterpiece-painted-in-an-ms-paint-clone-with-11-066-strokes.md#中文) | [@venturetwins](https://x.com/venturetwins) | 只有需求原话 | 1.7 万 |
| 132 | [一笔一笔画出的马斯克写实油画](cases/painting/132-realistic-oil-portrait-of-elon-musk-painted-stroke-by-stroke.md#中文) | [@DeaglePc](https://x.com/DeaglePc) | 完整原文 | 210 |
| 133 | [用自制工具画出做自己的感觉](cases/painting/133-oil-painting-of-what-being-the-model-feels-like.md#中文) | [@ZryMiller](https://x.com/ZryMiller) | 完整原文 | 900 |
| 134 | [能画出的最复杂原创画作](cases/painting/134-the-most-complex-original-painting-it-could-make.md#中文) | [@imjustnewatai](https://x.com/imjustnewatai) | 完整原文 | 4,511 |
| 135 | [虚构画家 Odile 的 6,300 笔画作](cases/painting/135-painting-by-a-fictional-painter-odile-in-6-300-python.md#中文) | [@HelaliBillel](https://x.com/HelaliBillel) | 未公开 | 59 |
| 136 | [用一粒种子的一生讲业力](cases/painting/136-karma-told-through-the-life-of-a-seed-in-13-paintings.md#中文) | [@anand_bongir](https://x.com/anand_bongir) | 未公开 | 41 |
| 137 | [用代码画的瑞士湖景油画](cases/painting/137-oil-painting-of-a-swiss-lake-scene.md#中文) | [@MrTacticalX](https://x.com/MrTacticalX) | 未公开 | 1,019 |
| 138 | [全自动做出的绘画引擎](cases/painting/138-fully-autonomous-painting-engine-in-2-101-lines-of.md#中文) | [@SweetRetry](https://x.com/SweetRetry) | 未公开 | 4 |
| 139 | [纯 JS 代码画的蒙娜丽莎](cases/painting/139-mona-lisa-recreated-in-pure-js-code.md#中文) | [@chetaslua](https://x.com/chetaslua) | 未公开 | 1 万 |
| 140 | [模拟油彩混色画布上的 Sam Altman](cases/painting/140-sam-altman-portrait-on-a-canvas-that-mixes-paint.md#中文) | [@internetphysics](https://x.com/internetphysics) | 未公开 | 6.6 万 |
| 141 | [一次生成的代码绘画作品](cases/painting/141-code-painting-generated-in-a-single-pass.md#中文) | [@devsvn2](https://x.com/devsvn2) | 未公开 | 25.4 万 |
| 142 | [每一笔都由 Fable 5.2 画出](cases/painting/142-artwork-with-every-brushstroke-made-by-fable-5-2.md#中文) | [@yuwen_lu_](https://x.com/yuwen_lu_) | 未公开 | 1,264 |
| 143 | [用画笔动画讲自己的一生](cases/painting/143-brushstroke-animation-of-the-model-s-own-life-story.md#中文) | [@iumarmirza](https://x.com/iumarmirza) | 只有需求原话 | 278 |
| 144 | [印象派风格的像素画](cases/painting/144-pixel-art-in-an-impressionist-style.md#中文) | [@aimi_teno](https://x.com/aimi_teno) | 未公开 | 63 |
| 145 | [311,905 笔重画波拉波拉岛](cases/painting/145-bora-bora-photo-repainted-in-311-905-strokes.md#中文) | [@sonuv_dev](https://x.com/sonuv_dev) | 未公开 | 708 |

## 自己动手做一个

仓库里的两套起步脚本是 apimodels.app 自己写、自己跑过的，不是上面作者的作品。

- [starter/blender](starter/blender)：`scene.py` 全程用 Python 搭一个小动画场景并渲染。Apple M4、Blender 5.3、EEVEE 实测：`--preview` 出 3 张预览帧约 26 秒，`--final` 出 72 帧 1280×720 的 H.264 MP4 用了 77 秒。用的是 Blender 5 的新写法，不会报弃用警告。图文教程：[用 Claude Code 写 Blender Python](https://apimodels.app/zh/blender-python-claude-code)。
- [starter/threejs](starter/threejs)：`scene.html` 暴露 `window.renderAt(t)`，`capture.mjs` 用 Playwright 逐帧截图（走 SwiftShader，不需要显卡），再用 FFmpeg 编码成 MP4。我们本机 6.5 秒截完 120 帧 1280×720。图文教程：[用 Claude Code 写 Three.js](https://apimodels.app/zh/claude-code-threejs)。
- 写提示词：[Claude Fable 5.2 提示词指南](https://apimodels.app/zh/claude-fable-5-2-prompting-guide)，整理了 Anthropic 官方建议，另附 6 个模板。

想让 Claude Code 通过 apimodels.app 跑 Fable 5.2，设三个环境变量即可（[完整配置](https://apimodels.app/zh/claude-code-fable-5-2)）：

```bash
export ANTHROPIC_BASE_URL="https://api.apimodels.app"
export ANTHROPIC_AUTH_TOKEN="你的 apimodels key"
export ANTHROPIC_MODEL="claude-fable-5-2"
claude
```

## 常见问题

### Claude Fable 5.2 能直接生成视频、音乐或画吗？

不能直接生成。Fable 5.2 输入文字和图片、输出文字。这里每件作品都是它写的代码渲染出来的：Blender Python 交给 Blender 渲染，Three.js / WebGL 网页由无头浏览器逐帧截图，声音用 Web Audio 或 numpy 合成，画作靠画布上的笔触引擎，最后用 FFmpeg 编码。在聊天窗口里你拿到的是代码或一个能打开的 HTML 页面；要直接拿到 MP4，得用能执行命令的 agent，比如 Claude Code。

### 这些真的是「一句提示词」做出来的吗？

有一些是。FPS 小关卡、鹈鹕骑车、浏览器里的 Minecraft 克隆，开头都只有一两句话。但「一句提示词」很少等于「秒回一次」：作者自述的运行时间从约 20 分钟到 8 小时不等，有一个开放世界游戏连续做了 7 天，不少人中途还追加了指令。另一些案例用的是约 6,000 到 9,400 字符的长提示词。每个案例页都标明了：是完整原文、只是一句需求原话，还是没公开。

### 做这些要花多少钱？

按作者自己公布的：两个像素风开关分别 $7.48 和 $8.43，巨石阵场景 $21，瑞士湖景油画 $22.62，2,000 行的 Three.js 短片 $34.96，冰之大教堂（和 Opus 同题对比）$81.10，8 小时的 FPS 关卡约 $550。4K Blender 渲染租 10 张 GPU 花了 $5.75（这是 GPU 费用）。这类任务主要花在输出 token 上：鹈鹕那次输出约 110 万 token，在 apimodels.app 按每百万 $24 算，输出部分约 $26；按 Anthropic 官方每百万 $40 算约 $44。

### 需要装什么？

一个能执行命令、接上 Fable 5.2 的 agent（Claude Code 或同类工具）；网页渲染类需要 Node.js、Playwright 和 FFmpeg；Blender 类需要 Blender 5.x，用到 Blender MCP 的案例还要装这个插件。Cycles 渲染有显卡更快，EEVEE 在笔记本上就能跑。音乐类用浏览器里的 Web Audio、numpy 或 LilyPond。

### effort 选哪一档？

API 上 Fable 5.2 默认 high；Claude Code 和 Claude 应用默认 medium。一次跑很久、失败重来代价比多花 token 更大的任务，可以往上调；小修小改用 medium 就够。

### 怎么通过 apimodels.app 调用 Claude Fable 5.2？

模型 ID 用 `claude-fable-5-2`，走 `/v1/messages`（Claude Code、Anthropic SDK、Cursor）或兼容 OpenAI 的 `/v1/chat/completions`，一个 apimodels.app 的 key 就行。按 token 计费：每百万输入 $4.80、输出 $24、缓存读 $0.12，不用订阅。失败的请求不收费，所有公开模型近 30 天的成功率都公布在 [apimodels.app/reliability](https://apimodels.app/zh/reliability)。

## 署名、版权与许可

- **作品归原作者所有。** 本仓库不存放他们的视频、图片或代码，每个案例都链到原帖。
- **提示词署名并附链接。** 400 字符以内的公开提示词全文收录；9 份更长的（546 到 9,411 字符）只放节选，附我们自己整理的结构说明和全文链接；没公开的一律不补写。商用前请先看原帖。
- 有两份长提示词是通过另一个合集 [yihui-dev/awesome-fable5-2-videos](https://github.com/yihui-dev/awesome-fable5-2-videos) 找到的，对应页面已注明。
- 有些案例复刻或致敬了已有的游戏、电影、画作或品牌，或画了真实人物，这些素材的权利归其所有者。
- **我们自己写的内容**（案例介绍和结构说明、「好提示词都做了什么」、起步脚本、`data/cases.json`）采用 [CC BY 4.0](LICENSE) 许可，转用请署名 apimodels.app 并附链接。
- 如果你是其中某个作品的作者，想撤下或更正署名，开一个 issue，我们会尽快处理。

通过 apimodels.app 调用 Claude Fable 5.2：[模型页](https://apimodels.app/zh/models/claude-fable-5-2) · [API 文档](https://apimodels.app/zh/docs/llm) · [更多 Fable 5.2 玩法](https://apimodels.app/zh/blog/claude-fable-5-2-use-cases)
