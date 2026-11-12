// capture.mjs: render every frame of a page that exposes window.renderAt(t)
// usage: node capture.mjs scene.html frames 30
import { chromium } from 'playwright'
import { mkdirSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const [file, outDir = 'frames', fps = 30] = process.argv.slice(2)
mkdirSync(outDir, { recursive: true })

const browser = await chromium.launch({
  executablePath: process.env.CHROME_BIN || undefined, // optional: an existing Chrome
  args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'], // WebGL without a GPU
})
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
page.on('pageerror', (e) => console.error('page error:', e.message))
await page.goto(pathToFileURL(resolve(file)).href + '?capture=1')
await page.waitForFunction(() => typeof window.renderAt === 'function')

const frames = Math.round((await page.evaluate(() => window.DURATION)) * fps)
for (let i = 0; i < frames; i++) {
  await page.evaluate((t) => window.renderAt(t), i / fps)
  await page.locator('canvas').screenshot({ path: `${outDir}/${String(i).padStart(4, '0')}.png` })
}
console.log(`${frames} frames written to ${outDir}/`)
await browser.close()
