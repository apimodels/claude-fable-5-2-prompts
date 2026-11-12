# Claude Fable 5.2 Prompts: 145 Creative Coding Cases

English · [简体中文](README.zh-CN.md)

145 things people made with Claude Fable 5.2 in its first week, from Blender films and Three.js scenes to games, fight animations, music and paintings, every one of them produced from code the model wrote. Each case is credited to its creator and linked to the original post on X, with the prompt word for word where the creator published it.

Disclosure: this collection is curated by [apimodels.app](https://apimodels.app), the API platform I work on. apimodels.app is a multi-model API gateway: one API key and Anthropic- and OpenAI-compatible endpoints for Claude Fable 5.2 and more than 150 other image, video, audio and language models. The two starters in [starter/](starter) were written and run by us; everything under [cases/](cases) is other people's work, described by us.

## In one paragraph

Claude Fable 5.2 (model id `claude-fable-5-2`, released by Anthropic on 9 November 2026) is a language model: it takes text and images and returns text, with a 1M-token context window and up to 128K output tokens. It does not render pixels or synthesise sound by itself. Every film, game, song and painting below came from code it wrote, such as Blender Python, Three.js and raw WebGL, Canvas, Web Audio, numpy or LilyPond, which an agent like Claude Code ran, rendered and usually encoded with FFmpeg. Many of the best-known results started from one or two sentences, but the runs behind them were long: the pelican film wrote about 4,800 lines of Python in a session of about 1.1M output tokens, and the FPS level ran for 8 hours at about $550 by its author's account. The 145 cases were posted on X between 4 and 11 November 2026; the few posted before 9 November are pre-release tests their authors labelled "Fable 5.5". 38 cases have the full prompt as the creator published it (9 long briefs are excerpted here, with an outline), 20 have only the creator's one-line request, and 87 were never published; we never fill in an unpublished prompt. On apimodels.app, Fable 5.2 costs $4.80 per 1M input tokens and $24 per 1M output tokens, against Anthropic's $8 / $40 list.

## Contents

- [Blender 3D with Python](#blender-3d-with-python) (21)
- [Three.js Scenes and Animation](#threejs-scenes-and-animation) (24)
- [Motion Graphics and Launch Videos](#motion-graphics-and-launch-videos) (21)
- [Games](#games) (19)
- [Character Action and Fights](#character-action-and-fights) (21)
- [Music in Code](#music-in-code) (18)
- [Painting in Code](#painting-in-code) (21)
- [Start here: the ten most-viewed cases](#start-here-the-ten-most-viewed-cases)
- [What the best briefs do](#what-the-best-briefs-do)
- [Make one yourself](#make-one-yourself)
- [FAQ](#faq)
- [Credits, copyright and licence](#credits-copyright-and-licence)

Each case has its own page under [cases/](cases) with the creator, the original post, what was made, the prompt status and, where published, the prompt. Views and likes are as of 11 November 2026. A machine-readable copy of everything is in [data/cases.json](data/cases.json).

## Start here: the ten most-viewed cases

1. [Realistic AAA-style FPS level built over 8 hours](cases/games/067-realistic-aaa-style-fps-level-built-over-8-hours.md) by @felixrieseberg, about 3.9M views (full prompt)
2. [Open-world game developed over 7 straight days](cases/games/074-open-world-game-developed-over-7-straight-days.md) by @mattshumer_, about 815K views (not published)
3. [13-shot Blender short with a MacBook and Clawd, made on a livestream](cases/blender/003-13-shot-blender-short-with-a-macbook-and-clawd-made-on-a.md) by @rileybrown, about 810K views (not published)
4. [Photoreal oil painting in 700,000 strokes](cases/painting/125-photoreal-oil-painting-in-700-000-strokes.md) by @jkeatn, about 546K views (request only)
5. [Small boat sailing through 8 worlds, with a Fable-made trailer score](cases/games/069-small-boat-sailing-through-8-worlds-with-a-fable-made.md) by @kevin_t_ngo, about 462K views (not published)
6. [Paintings made after first inventing a painter persona](cases/painting/126-paintings-made-after-first-inventing-a-painter-persona.md) by @jkeatn, about 436K views (not published)
7. [Original Vocaloid love song featuring Teto](cases/music/109-original-vocaloid-love-song-featuring-teto.md) by @peach2k2, about 386K views (request only)
8. [Prehistoric watering hole with dinosaurs, built in Blender with Python](cases/blender/002-prehistoric-watering-hole-with-dinosaurs-built-in-blender.md) by @jeremyberman, about 282K views (not published)
9. [Code painting generated in a single pass](cases/painting/141-code-painting-generated-in-a-single-pass.md) by @devsvn2, about 254K views (not published)
10. [Harry Potter and Fortnite mashup game](cases/games/073-harry-potter-and-fortnite-mashup-game.md) by @mattshumer_, about 169K views (full prompt)

## What the best briefs do

These patterns come from the 38 published prompts in this collection.

- **Say what "done" looks like, then let it take the time.** The pelican prompt is three sentences, but it names the deliverable (a finished video file), the bar (believable anatomy, a drivetrain that works, real-world lighting) and gives explicit permission to work long: "Take the time it needs."
- **Pin the design with numbers, not adjectives.** The anime locomotive brief gives lengths in metres, a 120-frame transformation in five 24-frame stages and a 144 bpm music grid. The zombie eagle brief sets a triangle budget, texture sizes and a file-size limit. Numbers give the model something to check its work against.
- **Make every frame a function of time.** For browser work, ask for one self-contained page that exposes `window.renderAt(t)`, as the voxel Paris brief does, so a headless browser can capture any frame on demand at a steady frame rate. In Blender the equivalent is a script that sets every state per frame; the anime brief calls it a "story clock".
- **Make it check its own renders before the expensive one.** The strongest briefs end with checks: render six key frames and review them (the zombie hand), test every frame for parts passing through each other or wheels slipping (the anime short), look at stills from both sides of every cut (the robot night market). Fable 5.2 reads images, so the review loop runs on stills.
- **Put stops and a cost gate in front of anything paid.** The robot night-market brief stops twice for approval; the zombie hand brief makes it quote the cloud GPU job, with expected and maximum credits, and wait for a yes. Reported spends in this collection run from $5.75 of rented GPU time for a 4K Blender render to about $550 for an 8-hour game build.
- **Give it a reason or a persona when the task is open.** The most-liked painting post in the collection had the model invent a painter persona before it painted (@jkeatn), and one painter asked it to show "what it feels like to be you" (@ZryMiller). One-liners can travel too: "invent a new musical form" drew about 132K views.
- **Choose the effort level on purpose.** Creators here report medium (an open-source trailer), High (a lighthouse scene) and Extra High (a Bach chorale in LilyPond). On the API, Fable 5.2 defaults to high effort; Claude Code and the Claude apps default to medium, per Anthropic's launch post.

## Blender 3D with Python

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 1 | [Photoreal 3D pelican riding a bicycle, driven from Claude Code](cases/blender/001-photoreal-3d-pelican-riding-a-bicycle-driven-from-claude.md) | [@techfren](https://x.com/techfren) | Full prompt | 163K |
| 2 | [Prehistoric watering hole with dinosaurs, built in Blender with Python](cases/blender/002-prehistoric-watering-hole-with-dinosaurs-built-in-blender.md) | [@jeremyberman](https://x.com/jeremyberman) | Not published | 282K |
| 3 | [13-shot Blender short with a MacBook and Clawd, made on a livestream](cases/blender/003-13-shot-blender-short-with-a-macbook-and-clawd-made-on-a.md) | [@rileybrown](https://x.com/rileybrown) | Not published | 810K |
| 4 | [Steam locomotive transforms into a robot in a 2D anime short](cases/blender/004-steam-locomotive-transforms-into-a-robot-in-a-2d-anime-short.md) | [@0kncn](https://x.com/0kncn) | Excerpt + outline | 69K |
| 5 | [Game-ready 3D zombie war eagle built through Blender MCP](cases/blender/005-game-ready-3d-zombie-war-eagle-built-through-blender-mcp.md) | [@maxt3chno](https://x.com/maxt3chno) | Excerpt + outline | 21K |
| 6 | [Jerusalem in the final week of Jesus's life, rebuilt in Blender](cases/blender/006-jerusalem-in-the-final-week-of-jesus-s-life-rebuilt-in.md) | [@kplikethebird](https://x.com/kplikethebird) | Full prompt | 10K |
| 7 | [Photoreal Bugatti Tourbillon render from one prompt and a reference image](cases/blender/007-photoreal-bugatti-tourbillon-render-from-one-prompt-and-a.md) | [@xikhar](https://x.com/xikhar) | Not published | 112K |
| 8 | [Star Wars Blender Bench: the First Battle of Geonosis](cases/blender/008-star-wars-blender-bench-the-first-battle-of-geonosis.md) | [@adityavg13](https://x.com/adityavg13) | Not published | 44K |
| 9 | [Rigged cartoon zombie hand that crawls and does a backflip](cases/blender/009-rigged-cartoon-zombie-hand-that-crawls-and-does-a-backflip.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Excerpt + outline | 63K |
| 10 | [Transformer truck with an animation of it transforming](cases/blender/010-transformer-truck-with-an-animation-of-it-transforming.md) | [@camperaigg](https://x.com/camperaigg) | Full prompt | 3,471 |
| 11 | [Howl's Moving Castle with its internal machinery shown](cases/blender/011-howl-s-moving-castle-with-its-internal-machinery-shown.md) | [@camperaigg](https://x.com/camperaigg) | Full prompt | 3,019 |
| 12 | [Mechanical heart with its inner workings revealed in Blender](cases/blender/012-mechanical-heart-with-its-inner-workings-revealed-in-blender.md) | [@camperaigg](https://x.com/camperaigg) | Full prompt | 5,836 |
| 13 | [Blender 3D animation test from a Japanese creator](cases/blender/013-blender-3d-animation-test-from-a-japanese-creator.md) | [@ICO_AIvideo](https://x.com/ICO_AIvideo) | Not published | 104K |
| 14 | [Blender short finished with zero human feedback](cases/blender/014-blender-short-finished-with-zero-human-feedback.md) | [@HyunSeob_](https://x.com/HyunSeob_) | Not published | 583 |
| 15 | [Story of Fable's own invention, told as an 18-shot 4K short](cases/blender/015-story-of-fable-s-own-invention-told-as-an-18-shot-4k-short.md) | [@CalebJones800](https://x.com/CalebJones800) | Request only | 113 |
| 16 | [Temple of a Thousand Lamps, compared with Opus on the same prompt](cases/blender/016-temple-of-a-thousand-lamps-compared-with-opus-on-the-same.md) | [@akshar_ai](https://x.com/akshar_ai) | Not published | 1,498 |
| 17 | [Airbnb house rebuilt as a 3D walkthrough from 4 screenshots](cases/blender/017-airbnb-house-rebuilt-as-a-3d-walkthrough-from-4-screenshots.md) | [@WalidBou07](https://x.com/WalidBou07) | Full prompt | 131 |
| 18 | [Glass house through the four seasons, animated in Blender](cases/blender/018-glass-house-through-the-four-seasons-animated-in-blender.md) | [@lynzhong_growth](https://x.com/lynzhong_growth) | Not published | 5,214 |
| 19 | [Perpetual calendar clock mechanism animated in Blender](cases/blender/019-perpetual-calendar-clock-mechanism-animated-in-blender.md) | [@MakeAI_CEO](https://x.com/MakeAI_CEO) | Not published | 2,486 |
| 20 | [Low-poly floating island scene made with Blender MCP](cases/blender/020-low-poly-floating-island-scene-made-with-blender-mcp.md) | [@rewind02](https://x.com/rewind02) | Full prompt | 923 |
| 21 | [Blender short from 1,110 lines of Python in 16.4 minutes](cases/blender/021-blender-short-from-1-110-lines-of-python-in-16-4-minutes.md) | [@FreshOutofBeta](https://x.com/FreshOutofBeta) | Not published | 63 |

## Three.js Scenes and Animation

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 22 | [Mech archer firing an arrow through the ocean](cases/threejs/022-mech-archer-firing-an-arrow-through-the-ocean.md) | [@camperaigg](https://x.com/camperaigg) | Request only | 1,111 |
| 23 | [Falling into a black hole in three.js](cases/threejs/023-falling-into-a-black-hole-in-three-js.md) | [@camperaigg](https://x.com/camperaigg) | Request only | 13K |
| 24 | [Match strike in slow motion, built in three.js](cases/threejs/024-match-strike-in-slow-motion-built-in-three-js.md) | [@camperaigg](https://x.com/camperaigg) | Request only | 16K |
| 25 | [Rowing into a 31 m wave in three.js](cases/threejs/025-rowing-into-a-31-m-wave-in-three-js.md) | [@camperaigg](https://x.com/camperaigg) | Request only | 19K |
| 26 | [Riding a lightning bolt from cloud to ground](cases/threejs/026-riding-a-lightning-bolt-from-cloud-to-ground.md) | [@camperaigg](https://x.com/camperaigg) | Request only | 106K |
| 27 | [83-second animated short rendered frame by frame in three.js](cases/threejs/027-83-second-animated-short-rendered-frame-by-frame-in-three-js.md) | [@noisyb0y1](https://x.com/noisyb0y1) | Not published | 12K |
| 28 | [Voxel Paris as a 14-second three.js animation](cases/threejs/028-voxel-paris-as-a-14-second-three-js-animation.md) | [@RezAIT00](https://x.com/RezAIT00) | Excerpt + outline | 4,436 |
| 29 | [Robot night market short film with procedural sound](cases/threejs/029-robot-night-market-short-film-with-procedural-sound.md) | [@evaninfra](https://x.com/evaninfra) | Excerpt + outline | 53 |
| 30 | [Interactive Stonehenge winter solstice sunrise in three.js](cases/threejs/030-interactive-stonehenge-winter-solstice-sunrise-in-three-js.md) | [@MeltTheManual](https://x.com/MeltTheManual) | Not published | 153 |
| 31 | [How an ASML EUV lithography machine works, in three.js](cases/threejs/031-how-an-asml-euv-lithography-machine-works-in-three-js.md) | [@miki_code](https://x.com/miki_code) | Not published | 182 |
| 32 | [Cutaway animation of a jet engine in three.js](cases/threejs/032-cutaway-animation-of-a-jet-engine-in-three-js.md) | [@renoiseai](https://x.com/renoiseai) | Not published | 820 |
| 33 | [Particle effect with 320,000 particles in three.js](cases/threejs/033-particle-effect-with-320-000-particles-in-three-js.md) | [@mdjunaidap](https://x.com/mdjunaidap) | Not published | 1,216 |
| 34 | [Mars rover scene in three.js](cases/threejs/034-mars-rover-scene-in-three-js.md) | [@koss_ai](https://x.com/koss_ai) | Not published | 244 |
| 35 | [Capybara-themed animation built in three.js](cases/threejs/035-capybara-themed-animation-built-in-three-js.md) | [@anstapnever](https://x.com/anstapnever) | Not published | 246 |
| 36 | [4 Elements: water, fire, wind and earth from each model](cases/threejs/036-4-elements-water-fire-wind-and-earth-from-each-model.md) | [@orcdev](https://x.com/orcdev) | Not published | 3,592 |
| 37 | [Monica's apartment from Friends rebuilt in three.js](cases/threejs/037-monica-s-apartment-from-friends-rebuilt-in-three-js.md) | [@chetaslua](https://x.com/chetaslua) | Not published | 13K |
| 38 | [Cathedral of ice, run head to head with Opus](cases/threejs/038-cathedral-of-ice-run-head-to-head-with-opus.md) | [@QQTeng](https://x.com/QQTeng) | Request only | 76K |
| 39 | [Manhattan at night: Fable versus Opus on one prompt](cases/threejs/039-manhattan-at-night-fable-versus-opus-on-one-prompt.md) | [@KernelChai](https://x.com/KernelChai) | Request only | 629 |
| 40 | [Deep Dive Switch: an underwater world inside a slider](cases/threejs/040-deep-dive-switch-an-underwater-world-inside-a-slider.md) | [@N1njaCodex](https://x.com/N1njaCodex) | Excerpt + outline | 3,992 |
| 41 | [Daybreak Switch: a cozy room from night to morning](cases/threejs/041-daybreak-switch-a-cozy-room-from-night-to-morning.md) | [@vib3coded](https://x.com/vib3coded) | Excerpt + outline | 94K |
| 42 | [Paris in 1940, built in three.js from Higgsfield references](cases/threejs/042-paris-in-1940-built-in-three-js-from-higgsfield-references.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Not published | 15K |
| 43 | [Lighthouse in a Storm at High effort](cases/threejs/043-lighthouse-in-a-storm-at-high-effort.md) | [@rohit3a](https://x.com/rohit3a) | Not published | 1,857 |
| 44 | [Photoreal lighthouse scene from the author's own prompt](cases/threejs/044-photoreal-lighthouse-scene-from-the-author-s-own-prompt.md) | [@viewsfrom02108](https://x.com/viewsfrom02108) | Not published | 304 |
| 45 | [Discovery, a 101-second short film in three.js](cases/threejs/045-discovery-a-101-second-short-film-in-three-js.md) | [@YinYangYoeshi](https://x.com/YinYangYoeshi) | Not published | 449 |

## Motion Graphics and Launch Videos

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 46 | [Motion graphics tribute to ChatGPT's fourth anniversary](cases/motion-graphics/046-motion-graphics-tribute-to-chatgpt-s-fourth-anniversary.md) | [@Khazix0918](https://x.com/Khazix0918) | Full prompt | 91K |
| 47 | [30-second motion graphics portfolio piece for a résumé](cases/motion-graphics/047-30-second-motion-graphics-portfolio-piece-for-a-resume.md) | [@Leviwoyun](https://x.com/Leviwoyun) | Full prompt | 24K |
| 48 | [15-second motion designer showreel](cases/motion-graphics/048-15-second-motion-designer-showreel.md) | [@himanshutwtxs](https://x.com/himanshutwtxs) | Full prompt | 1,215 |
| 49 | [Most impressive motion design video, with a 40,000-bird flock](cases/motion-graphics/049-most-impressive-motion-design-video-with-a-40-000-bird-flock.md) | [@techfren](https://x.com/techfren) | Request only | 1,002 |
| 50 | [Mograph animation explaining how LLMs work](cases/motion-graphics/050-mograph-animation-explaining-how-llms-work.md) | [@MatthewBerman](https://x.com/MatthewBerman) | Request only | 7,594 |
| 51 | [Clawd building and releasing Claude Fable 5.2, animated](cases/motion-graphics/051-clawd-building-and-releasing-claude-fable-5-2-animated.md) | [@other__reality](https://x.com/other__reality) | Full prompt | 13K |
| 52 | [90-second Fable 5.2 self-promotion video](cases/motion-graphics/052-90-second-fable-5-2-self-promotion-video.md) | [@yasu_919](https://x.com/yasu_919) | Full prompt | 189 |
| 53 | [Product launch video for an API website](cases/motion-graphics/053-product-launch-video-for-an-api-website.md) | [@PeetuKupiainen](https://x.com/PeetuKupiainen) | Full prompt | 242 |
| 54 | [The History of Writing, a photoreal historical time-lapse](cases/motion-graphics/054-the-history-of-writing-a-photoreal-historical-time-lapse.md) | [@rileybrown](https://x.com/rileybrown) | Excerpt + outline | 47K |
| 55 | [Japanese explainer on just how capable Fable 5.2 is](cases/motion-graphics/055-japanese-explainer-on-just-how-capable-fable-5-2-is.md) | [@tankazunori0914](https://x.com/tankazunori0914) | Full prompt | 1,131 |
| 56 | [Japanese showcase video of Fable 5.2 at full strength](cases/motion-graphics/056-japanese-showcase-video-of-fable-5-2-at-full-strength.md) | [@marcy_sns](https://x.com/marcy_sns) | Full prompt | 983 |
| 57 | [15-second farewell to Opus 5.5 as Fable 5.2 arrives](cases/motion-graphics/057-15-second-farewell-to-opus-5-5-as-fable-5-2-arrives.md) | [@kaif9998](https://x.com/kaif9998) | Full prompt | 1,588 |
| 58 | [Launch-day animation built to be shared](cases/motion-graphics/058-launch-day-animation-built-to-be-shared.md) | [@ici_dab](https://x.com/ici_dab) | Full prompt | 89 |
| 59 | [60-second Fable 5.2 launch film made with Opus 5.5 subagents](cases/motion-graphics/059-60-second-fable-5-2-launch-film-made-with-opus-5-5-subagents.md) | [@grafikcem](https://x.com/grafikcem) | Full prompt | 185 |
| 60 | [Its own launch video, made with code only](cases/motion-graphics/060-its-own-launch-video-made-with-code-only.md) | [@furkancavlakcom](https://x.com/furkancavlakcom) | Full prompt | 36K |
| 61 | [Animated social media trailer for an open-source project](cases/motion-graphics/061-animated-social-media-trailer-for-an-open-source-project.md) | [@midudev](https://x.com/midudev) | Full prompt | 97K |
| 62 | [2D night-time animation of a man entering a lighthouse](cases/motion-graphics/062-2d-night-time-animation-of-a-man-entering-a-lighthouse.md) | [@talhaXclusively](https://x.com/talhaXclusively) | Full prompt | 48 |
| 63 | [One-pass 9:16 vertical edit with animations and mographs](cases/motion-graphics/063-one-pass-9-16-vertical-edit-with-animations-and-mographs.md) | [@The_Alex](https://x.com/The_Alex) | Request only | 3,945 |
| 64 | [Animated product explainer for Convex](cases/motion-graphics/064-animated-product-explainer-for-convex.md) | [@Rasmic](https://x.com/Rasmic) | Not published | 12K |
| 65 | [Launch promotional video made with Fable 5.2](cases/motion-graphics/065-launch-promotional-video-made-with-fable-5-2.md) | [@DoctorYev](https://x.com/DoctorYev) | Not published | 1,630 |
| 66 | [Animated explainer of the AI 2027 document](cases/motion-graphics/066-animated-explainer-of-the-ai-2027-document.md) | [@Btheriot](https://x.com/Btheriot) | Not published | 51 |

## Games

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 67 | [Realistic AAA-style FPS level built over 8 hours](cases/games/067-realistic-aaa-style-fps-level-built-over-8-hours.md) | [@felixrieseberg](https://x.com/felixrieseberg) | Full prompt | 3.9M |
| 68 | [First-person shooter written in three.js](cases/games/068-first-person-shooter-written-in-three-js.md) | [@JaydenDavisNC](https://x.com/JaydenDavisNC) | Not published | 43K |
| 69 | [Small boat sailing through 8 worlds, with a Fable-made trailer score](cases/games/069-small-boat-sailing-through-8-worlds-with-a-fable-made.md) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | Not published | 462K |
| 70 | [Gilt & Gutter, a game built with Fable](cases/games/070-gilt-gutter-a-game-built-with-fable.md) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | Not published | 101K |
| 71 | [Game with an AAA-quality look, made in 4 hours](cases/games/071-game-with-an-aaa-quality-look-made-in-4-hours.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Not published | 19K |
| 72 | [Gears of War-style game built in Unreal](cases/games/072-gears-of-war-style-game-built-in-unreal.md) | [@MatthewBerman](https://x.com/MatthewBerman) | Not published | 140K |
| 73 | [Harry Potter and Fortnite mashup game](cases/games/073-harry-potter-and-fortnite-mashup-game.md) | [@mattshumer_](https://x.com/mattshumer_) | Full prompt | 169K |
| 74 | [Open-world game developed over 7 straight days](cases/games/074-open-world-game-developed-over-7-straight-days.md) | [@mattshumer_](https://x.com/mattshumer_) | Not published | 815K |
| 75 | [Casual flying game over Lisbon, playable online](cases/games/075-casual-flying-game-over-lisbon-playable-online.md) | [@goncalo_canhoto](https://x.com/goncalo_canhoto) | Not published | 12K |
| 76 | [Hand-painted oil-paint game with 1.5 million brush strokes](cases/games/076-hand-painted-oil-paint-game-with-1-5-million-brush-strokes.md) | [@BlendiByl](https://x.com/BlendiByl) | Not published | 162K |
| 77 | [Full Minecraft clone running in the browser](cases/games/077-full-minecraft-clone-running-in-the-browser.md) | [@intheworldofai](https://x.com/intheworldofai) | Full prompt | 6,829 |
| 78 | [One-shot 3D basketball arena game in three.js](cases/games/078-one-shot-3d-basketball-arena-game-in-three-js.md) | [@joshvlc](https://x.com/joshvlc) | Excerpt + outline | 109 |
| 79 | [Reverse Scooby-Doo mystery game](cases/games/079-reverse-scooby-doo-mystery-game.md) | [@emollick](https://x.com/emollick) | Not published | 32K |
| 80 | [Go-kart racing game built with Fable 5.2](cases/games/080-go-kart-racing-game-built-with-fable-5-2.md) | [@petergyang](https://x.com/petergyang) | Not published | 32K |
| 81 | [Game in the style of Fall Guys](cases/games/081-game-in-the-style-of-fall-guys.md) | [@alexmichael](https://x.com/alexmichael) | Not published | 2,030 |
| 82 | [Horror game made in Roblox](cases/games/082-horror-game-made-in-roblox.md) | [@mihawkxxxxx](https://x.com/mihawkxxxxx) | Not published | 1,150 |
| 83 | [Open-source alchemy game on GitHub](cases/games/083-open-source-alchemy-game-on-github.md) | [@winchxyz](https://x.com/winchxyz) | Not published | 442 |
| 84 | [Fantasy game built with Fable 5.2](cases/games/084-fantasy-game-built-with-fable-5-2.md) | [@flxrnc](https://x.com/flxrnc) | Not published | 646 |
| 85 | [Playable pelican-on-a-bicycle mini game](cases/games/085-playable-pelican-on-a-bicycle-mini-game.md) | [@siennatries](https://x.com/siennatries) | Not published | 71 |

## Character Action and Fights

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 86 | [Stick-figure fight with slow motion and an Opus cost comparison](cases/character-action/086-stick-figure-fight-with-slow-motion-and-an-opus-cost.md) | [@DanielZambrini](https://x.com/DanielZambrini) | Not published | 33K |
| 87 | [The same stick-figure fight test: Gemini 4 Carbon vs Fable 5.2](cases/character-action/087-the-same-stick-figure-fight-test-gemini-4-carbon-vs-fable-5.md) | [@DanielZambrini](https://x.com/DanielZambrini) | Not published | 21K |
| 88 | [Stick-figure fight animation, compared with an earlier Fable 5.5 test](cases/character-action/088-stick-figure-fight-animation-compared-with-an-earlier-fable.md) | [@leo114119](https://x.com/leo114119) | Not published | 1,384 |
| 89 | [Stick-figure fight billed as cinematic, with effects](cases/character-action/089-stick-figure-fight-billed-as-cinematic-with-effects.md) | [@RJasonHA](https://x.com/RJasonHA) | Not published | 635 |
| 90 | [15-second stick-figure lightsaber duel, compared with Opus 5.5](cases/character-action/090-15-second-stick-figure-lightsaber-duel-compared-with-opus-5.md) | [@jiangjiangling](https://x.com/jiangjiangling) | Not published | 383 |
| 91 | [Diablo IV recreation in Blender with a rigged fighting character](cases/character-action/091-diablo-iv-recreation-in-blender-with-a-rigged-fighting.md) | [@ChengYi3629](https://x.com/ChengYi3629) | Not published | 320 |
| 92 | [Soulslike boss fight with an online version](cases/character-action/092-soulslike-boss-fight-with-an-online-version.md) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | Not published | 101K |
| 93 | [Iron Bamboo boss fight in 3,400 lines of three.js](cases/character-action/093-iron-bamboo-boss-fight-in-3-400-lines-of-three-js.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Not published | 14K |
| 94 | [Full three.js sword-fighting game from a single prompt](cases/character-action/094-full-three-js-sword-fighting-game-from-a-single-prompt.md) | [@FutureFlynn5](https://x.com/FutureFlynn5) | Not published | 40 |
| 95 | [Courtyard Kings, a fighting game with audio from ElevenLabs MCP](cases/character-action/095-courtyard-kings-a-fighting-game-with-audio-from-elevenlabs.md) | [@promodenstudio](https://x.com/promodenstudio) | Not published | 174 |
| 96 | [Raw Tripo model turned into a rigged game character in Blender](cases/character-action/096-raw-tripo-model-turned-into-a-rigged-game-character-in.md) | [@0xKense1](https://x.com/0xKense1) | Not published | 48K |
| 97 | [Armed and armored action character made with Tripo and Blender MCP](cases/character-action/097-armed-and-armored-action-character-made-with-tripo-and.md) | [@luccacerf](https://x.com/luccacerf) | Not published | 16K |
| 98 | [New enemy designed from scratch for a cartoon FPS](cases/character-action/098-new-enemy-designed-from-scratch-for-a-cartoon-fps.md) | [@whaledevstudios](https://x.com/whaledevstudios) | Request only | 1,231 |
| 99 | [AR boxing game with camera hand tracking](cases/character-action/099-ar-boxing-game-with-camera-hand-tracking.md) | [@TusharXo](https://x.com/TusharXo) | Not published | 334 |
| 100 | [3D action game in the style of Shadow Blade Zero](cases/character-action/100-3d-action-game-in-the-style-of-shadow-blade-zero.md) | [@ohmygameai](https://x.com/ohmygameai) | Not published | 754 |
| 101 | [3D action animation generated from a reference video](cases/character-action/101-3d-action-animation-generated-from-a-reference-video.md) | [@KHvostikk](https://x.com/KHvostikk) | Not published | 63K |
| 102 | [Kung fu cat built in code from spheres and cones](cases/character-action/102-kung-fu-cat-built-in-code-from-spheres-and-cones.md) | [@New202064737](https://x.com/New202064737) | Not published | 79 |
| 103 | [One-prompt action piece on Fable 5.2 at High effort](cases/character-action/103-one-prompt-action-piece-on-fable-5-2-at-high-effort.md) | [@tymarsha](https://x.com/tymarsha) | Not published | 265 |
| 104 | [Street Fighter 2 clone generated in one go](cases/character-action/104-street-fighter-2-clone-generated-in-one-go.md) | [@BertrandDiouly](https://x.com/BertrandDiouly) | Not published | 558 |
| 105 | [Action game generated in a single run on Spawn](cases/character-action/105-action-game-generated-in-a-single-run-on-spawn.md) | [@OneHitKillDev](https://x.com/OneHitKillDev) | Not published | 1,508 |
| 106 | [Overwatch-style third-person PvPvE hero brawler](cases/character-action/106-overwatch-style-third-person-pvpve-hero-brawler.md) | [@Pumpnasterr](https://x.com/Pumpnasterr) | Not published | 1,785 |

## Music in Code

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 107 | [Original symphony with a matching video](cases/music/107-original-symphony-with-a-matching-video.md) | [@imjustnewatai](https://x.com/imjustnewatai) | Request only | 142K |
| 108 | [Inventing a new musical form](cases/music/108-inventing-a-new-musical-form.md) | [@imjustnewatai](https://x.com/imjustnewatai) | Request only | 132K |
| 109 | [Original Vocaloid love song featuring Teto](cases/music/109-original-vocaloid-love-song-featuring-teto.md) | [@peach2k2](https://x.com/peach2k2) | Request only | 386K |
| 110 | [Bach-style 4-part chorale written in LilyPond](cases/music/110-bach-style-4-part-chorale-written-in-lilypond.md) | [@aug5thmusic](https://x.com/aug5thmusic) | Full prompt | 67K |
| 111 | [Composition from a carefully written prompt during the trial](cases/music/111-composition-from-a-carefully-written-prompt-during-the-trial.md) | [@GrayCan1392](https://x.com/GrayCan1392) | Not published | 145 |
| 112 | [Painting and music generated together in Python](cases/music/112-painting-and-music-generated-together-in-python.md) | [@wquguru](https://x.com/wquguru) | Not published | 3,425 |
| 113 | [Acid techno track made with Fable](cases/music/113-acid-techno-track-made-with-fable.md) | [@Masimo_Blue](https://x.com/Masimo_Blue) | Not published | 2,407 |
| 114 | [Trailer score for a small boat game from CC0 samples](cases/music/114-trailer-score-for-a-small-boat-game-from-cc0-samples.md) | [@kevin_t_ngo](https://x.com/kevin_t_ngo) | Not published | 2,776 |
| 115 | [Music composed in code, with a write-up of the process](cases/music/115-music-composed-in-code-with-a-write-up-of-the-process.md) | [@taka_claudecode](https://x.com/taka_claudecode) | Not published | 38 |
| 116 | [Big-studio explainer on what happens when you click a link](cases/music/116-big-studio-explainer-on-what-happens-when-you-click-a-link.md) | [@MojojojoHojo](https://x.com/MojojojoHojo) | Request only | 57 |
| 117 | [Outlandish real research paper recreated as a short video](cases/music/117-outlandish-real-research-paper-recreated-as-a-short-video.md) | [@ronginooth](https://x.com/ronginooth) | Full prompt | 102 |
| 118 | [Web Audio turntable with visuals and sound](cases/music/118-web-audio-turntable-with-visuals-and-sound.md) | [@JuanDHernandezG](https://x.com/JuanDHernandezG) | Not published | 30 |
| 119 | [Left to choose its own tools, it built Web Audio bells](cases/music/119-left-to-choose-its-own-tools-it-built-web-audio-bells.md) | [@Maaaaaaadiii](https://x.com/Maaaaaaadiii) | Request only | 169 |
| 120 | [Formant synthesizer from Higgsfield](cases/music/120-formant-synthesizer-from-higgsfield.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Not published | 12K |
| 121 | [Getting Fable to sing through code](cases/music/121-getting-fable-to-sing-through-code.md) | [@higgsfield_ai](https://x.com/higgsfield_ai) | Not published | 13K |
| 122 | [Sound design in Blender and Reaper from iPhone recordings](cases/music/122-sound-design-in-blender-and-reaper-from-iphone-recordings.md) | [@AmirMushich](https://x.com/AmirMushich) | Not published | 77K |
| 123 | [Former film composer's ambient music workstation with a co-writing agent](cases/music/123-former-film-composer-s-ambient-music-workstation-with-a-co.md) | [@FinanceYF5](https://x.com/FinanceYF5) | Not published | 1,361 |
| 124 | [Music video for a song with lyrics](cases/music/124-music-video-for-a-song-with-lyrics.md) | [@WesRoth](https://x.com/WesRoth) | Not published | 8,415 |

## Painting in Code

| # | Case | Creator | Prompt | Views |
| --- | --- | --- | --- | --- |
| 125 | [Photoreal oil painting in 700,000 strokes](cases/painting/125-photoreal-oil-painting-in-700-000-strokes.md) | [@jkeatn](https://x.com/jkeatn) | Request only | 546K |
| 126 | [Paintings made after first inventing a painter persona](cases/painting/126-paintings-made-after-first-inventing-a-painter-persona.md) | [@jkeatn](https://x.com/jkeatn) | Not published | 436K |
| 127 | [Persona series: works by the painter Dermot Hale](cases/painting/127-persona-series-works-by-the-painter-dermot-hale.md) | [@jkeatn](https://x.com/jkeatn) | Not published | 52K |
| 128 | [Persona series: the Tidewright paintings](cases/painting/128-persona-series-the-tidewright-paintings.md) | [@jkeatn](https://x.com/jkeatn) | Not published | 49K |
| 129 | [Ocean wave oil painting in 710,989 strokes](cases/painting/129-ocean-wave-oil-painting-in-710-989-strokes.md) | [@hoppycat](https://x.com/hoppycat) | Not published | 535 |
| 130 | [Cheek to Cheek, a painting in 801,582 strokes](cases/painting/130-cheek-to-cheek-a-painting-in-801-582-strokes.md) | [@hoppycat](https://x.com/hoppycat) | Not published | 376 |
| 131 | [Masterpiece painted in an MS Paint clone with 11,066 strokes](cases/painting/131-masterpiece-painted-in-an-ms-paint-clone-with-11-066-strokes.md) | [@venturetwins](https://x.com/venturetwins) | Request only | 17K |
| 132 | [Realistic oil portrait of Elon Musk, painted stroke by stroke](cases/painting/132-realistic-oil-portrait-of-elon-musk-painted-stroke-by-stroke.md) | [@DeaglePc](https://x.com/DeaglePc) | Full prompt | 210 |
| 133 | [Oil painting of what being the model feels like](cases/painting/133-oil-painting-of-what-being-the-model-feels-like.md) | [@ZryMiller](https://x.com/ZryMiller) | Full prompt | 900 |
| 134 | [The most complex original painting it could make](cases/painting/134-the-most-complex-original-painting-it-could-make.md) | [@imjustnewatai](https://x.com/imjustnewatai) | Full prompt | 4,511 |
| 135 | [Painting by a fictional painter, Odile, in 6,300 Python strokes](cases/painting/135-painting-by-a-fictional-painter-odile-in-6-300-python.md) | [@HelaliBillel](https://x.com/HelaliBillel) | Not published | 59 |
| 136 | [Karma told through the life of a seed in 13 paintings](cases/painting/136-karma-told-through-the-life-of-a-seed-in-13-paintings.md) | [@anand_bongir](https://x.com/anand_bongir) | Not published | 41 |
| 137 | [Oil painting of a Swiss lake scene](cases/painting/137-oil-painting-of-a-swiss-lake-scene.md) | [@MrTacticalX](https://x.com/MrTacticalX) | Not published | 1,019 |
| 138 | [Fully autonomous painting engine in 2,101 lines of TypeScript](cases/painting/138-fully-autonomous-painting-engine-in-2-101-lines-of.md) | [@SweetRetry](https://x.com/SweetRetry) | Not published | 4 |
| 139 | [Mona Lisa recreated in pure JS code](cases/painting/139-mona-lisa-recreated-in-pure-js-code.md) | [@chetaslua](https://x.com/chetaslua) | Not published | 10K |
| 140 | [Sam Altman portrait on a canvas that mixes paint realistically](cases/painting/140-sam-altman-portrait-on-a-canvas-that-mixes-paint.md) | [@internetphysics](https://x.com/internetphysics) | Not published | 66K |
| 141 | [Code painting generated in a single pass](cases/painting/141-code-painting-generated-in-a-single-pass.md) | [@devsvn2](https://x.com/devsvn2) | Not published | 254K |
| 142 | [Artwork with every brushstroke made by Fable 5.2](cases/painting/142-artwork-with-every-brushstroke-made-by-fable-5-2.md) | [@yuwen_lu_](https://x.com/yuwen_lu_) | Not published | 1,264 |
| 143 | [Brushstroke animation of the model's own life story](cases/painting/143-brushstroke-animation-of-the-model-s-own-life-story.md) | [@iumarmirza](https://x.com/iumarmirza) | Request only | 278 |
| 144 | [Pixel art in an Impressionist style](cases/painting/144-pixel-art-in-an-impressionist-style.md) | [@aimi_teno](https://x.com/aimi_teno) | Not published | 63 |
| 145 | [Bora Bora photo repainted in 311,905 strokes](cases/painting/145-bora-bora-photo-repainted-in-311-905-strokes.md) | [@sonuv_dev](https://x.com/sonuv_dev) | Not published | 708 |

## Make one yourself

The two starters in this repository were written and run by apimodels.app, not by the creators above.

- [starter/blender](starter/blender): `scene.py` builds a small animated scene entirely in Python and renders it. On Blender 5.3 with EEVEE on an Apple M4, `--preview` renders 3 frames in about 26 s and `--final` renders 72 frames at 1280×720 to an H.264 MP4 in 77 s. It uses Blender 5 API names, so it runs without deprecation warnings. Walkthrough: [Blender Python with Claude Code](https://apimodels.app/blender-python-claude-code).
- [starter/threejs](starter/threejs): `scene.html` exposes `window.renderAt(t)`, `capture.mjs` captures every frame with Playwright (SwiftShader, so no GPU is needed), and FFmpeg encodes the MP4. On our machine it captured 120 frames at 1280×720 in 6.5 s. Walkthrough: [Three.js with Claude Code](https://apimodels.app/claude-code-threejs).
- Writing the brief: the [Claude Fable 5.2 prompting guide](https://apimodels.app/claude-fable-5-2-prompting-guide) summarises Anthropic's guidance and adds six templates.

To run Claude Code on Fable 5.2 through apimodels.app, set three environment variables ([full setup](https://apimodels.app/claude-code-fable-5-2)):

```bash
export ANTHROPIC_BASE_URL="https://api.apimodels.app"
export ANTHROPIC_AUTH_TOKEN="your_apimodels_key"
export ANTHROPIC_MODEL="claude-fable-5-2"
claude
```

## FAQ

### Can Claude Fable 5.2 make a video, a song or a painting by itself?

Not directly. Fable 5.2 takes text and image input and returns text. Every piece here was rendered from code it wrote: Blender Python rendered by Blender, Three.js or WebGL pages captured by a headless browser, Web Audio or numpy for sound, canvas stroke engines for paintings, and FFmpeg to encode the result. In a chat window you get code or an HTML page you can open; to get an MP4 you need an agent that can run commands, such as Claude Code.

### Did these really come from one prompt?

Some did. The FPS level, the pelican film and the browser Minecraft clone started from one or two sentences. But "one prompt" rarely means one quick reply: reported run times range from about 20 minutes to 8 hours, one open-world game was built over 7 days, and several authors added follow-up messages. Other cases ran on briefs of about 6,000 to 9,400 characters. Each case page says whether the text is the full prompt, only the creator's one-line request, or unpublished.

### How much did these cost?

As the creators reported them: $7.48 and $8.43 for the two pixel-art switches, $21 for the Stonehenge scene, $22.62 for a Swiss lake painting, $34.96 for a 2,000-line Three.js short, $81.10 for an ice cathedral run side by side with Opus, and about $550 for the 8-hour FPS level. A 4K Blender render on 10 rented GPUs cost $5.75 in GPU time. This kind of work is output-heavy: the pelican run wrote about 1.1M output tokens, which is about $26 of output on apimodels.app at $24 per 1M, or about $44 at Anthropic's $40 list price.

### What do I need installed?

An agent that can run commands (Claude Code or similar) pointed at Fable 5.2; Node.js with Playwright and FFmpeg for anything rendered in a browser; Blender 5.x for the Blender cases, plus the Blender MCP add-on for the cases that used it. A GPU helps for Cycles, but EEVEE runs fine on a laptop. Music cases use Web Audio in the browser, numpy or LilyPond.

### Which effort level should I use?

Fable 5.2 defaults to high effort on the API; Claude Code and the Claude apps default to medium. Raise it for long one-shot builds where a failed run costs more than the extra tokens, and keep medium for small fixes and iterations.

### How do I call Claude Fable 5.2 through apimodels.app?

Use the model id `claude-fable-5-2` on `/v1/messages` (Claude Code, the Anthropic SDK, Cursor) or the OpenAI-compatible `/v1/chat/completions`, with one apimodels.app key. It is billed per token: $4.80 per 1M input, $24 per 1M output and $0.12 per 1M cache reads, with no subscription. Failed requests are not billed, and the 30-day success rate of every public model is published at [apimodels.app/reliability](https://apimodels.app/reliability).

## Credits, copyright and licence

- **The works belong to their creators.** This repository hosts none of their videos, images or code; every case links to the original post.
- **Prompts are quoted with credit and a link.** Published prompts of up to 400 characters are quoted in full. The 9 longer briefs (546 to 9,411 characters) are excerpted, with our own outline of how each one is built and a link to the full text. Unpublished prompts are never filled in. Check the original post before using a prompt commercially.
- Two of the long prompts were located through another collection, [yihui-dev/awesome-fable5-2-videos](https://github.com/yihui-dev/awesome-fable5-2-videos); their pages say so.
- Some cases recreate or pay homage to existing games, films, paintings or brands, or depict real people. The rights in that source material belong to its owners.
- **Our own material** (the case write-ups and outlines, "What the best briefs do", the starters and `data/cases.json`) is licensed under [CC BY 4.0](LICENSE). Please credit apimodels.app with a link.
- If you made one of these and want it removed or the credit corrected, open an issue and we'll handle it promptly.

Call Claude Fable 5.2 through apimodels.app: [model page](https://apimodels.app/models/claude-fable-5-2) · [API docs](https://apimodels.app/docs/llm) · [more Fable 5.2 use cases](https://apimodels.app/blog/claude-fable-5-2-use-cases)
