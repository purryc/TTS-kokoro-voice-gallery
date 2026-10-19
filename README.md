# Kokoro Voice Gallery

[中文](#中文说明) · [English](#english)

[中文试听页](https://purryc.github.io/kokoro-voice-gallery/) · [English gallery](https://purryc.github.io/kokoro-voice-gallery/en.html)

## 中文说明

157 个 Kokoro 官方预设音色的独立社区试听页。支持试听、搜索、语言与男女声筛选、浏览器本地收藏、MP3 下载。界面及来源页支持中英切换，切换时保留播放进度、筛选与收藏；试听文案保留实际朗读的原文。页面只播放预生成样音，无后端、无 API key、无浏览器内语音合成。

## 音色分布

| 语言 | 女声 | 男声 | 合计 |
|---|---:|---:|---:|
| 中文 | 59 | 49 | 108 |
| 英语 | 18 | 13 | 31 |
| 西班牙语 | 1 | 2 | 3 |
| 法语 | 1 | 0 | 1 |
| 印地语 | 2 | 2 | 4 |
| 意大利语 | 1 | 1 | 2 |
| 日语 | 4 | 1 | 5 |
| 葡萄牙语 | 1 | 2 | 3 |
| **合计** | **87** | **70** | **157** |

先列女声，再列男声；组内按中文、英语、其他语言排列，官方编号按自然顺序排序（001、002、…）。全库连续序号 001–157 是本站索引，原始官方音色 ID 保持不变。筛选后索引保持稳定。

## 本地使用

Python 3.10+。生成页面无需安装 Python 第三方库。

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8080 --directory site
```

打开 http://localhost:8080 。也可直接用浏览器打开 `site/index.html`，保留同级 `audio/` 文件夹。收藏仅保存在当前浏览器，不上传服务器。

## 文件结构

- `templates/index.html`：试听页源模板；`templates/about.html` 与 `templates/about-en.html`：中英文来源页。
- `data/i18n.json`：完整中英文界面文案。
- `data/voices.json`：完整音色数据、试听文案、上游固定版本及相对音频路径。
- `site/`：可部署页面及 157 段 MP3 音频；`index.html` 为中文，`en.html` 为英文。
- `scripts/build.py`：生成页面与分布表。
- `scripts/validate.py`：完整性、排序、音频与公开内容检查；检测到 ffprobe 时会逐个验证音频。

## 发布

`.github/workflows/pages.yml` 通过 GitHub Actions 验证并发布 `site/`。支持手动运行，也在 main 更新时运行。仓库设置的 Pages 来源需为 GitHub Actions。

## 模型与许可

Kokoro v1.0：54 音色；Kokoro v1.1-zh：103 音色。样音使用 Kokoro 0.9.4 在本地生成，语速 1.0；网页版本为 128 kbps MP3。文案为本项目试听文本，没有用户录音。

本项目为独立社区作品，非 Kokoro 官方网站，与模型作者无隶属或背书关系。
项目代码及项目原创资产采用 Apache-2.0。模型、音色及上游训练素材保留各自许可与署名。Apache 许可证保留英文正式文本。详见 [LICENSE](LICENSE) 和 [NOTICE.md](NOTICE.md)。模型权重、运行环境及缓存不包含在本仓库中。

---

## English

An independent community gallery of 157 official Kokoro preset voices. Preview samples, search, filter by language and female/male voice, save browser-local favorites, and download MP3 files. The interface and provenance pages are available in Chinese and English. Switching the interface language preserves playback position, filters and favorites; sample scripts remain in the language actually spoken. Audio is pre-generated: no backend, API key or in-browser speech synthesis is needed.

### Voice distribution

| Language | Female | Male | Total |
|---|---:|---:|---:|
| Chinese | 59 | 49 | 108 |
| English | 18 | 13 | 31 |
| Spanish | 1 | 2 | 3 |
| French | 1 | 0 | 1 |
| Hindi | 2 | 2 | 4 |
| Italian | 1 | 1 | 2 |
| Japanese | 4 | 1 | 5 |
| Portuguese | 1 | 2 | 3 |
| **Total** | **87** | **70** | **157** |

Female voices appear first, followed by male voices. Each group lists Chinese, English and then other languages, with official IDs naturally sorted (001, 002, …). Stable row numbers 001–157 are gallery indices; original official voice IDs remain unchanged. Filtering does not renumber the catalog.

### Run locally

Requires Python 3.10+. The build uses only the Python standard library.

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8080 --directory site
```

Open http://localhost:8080/en.html . You can also open `site/en.html` directly in a browser, keeping the sibling `audio/` folder. Favorites stay in the current browser and are never uploaded.

### Project structure

- `templates/index.html`: gallery source template; `templates/about.html` and `templates/about-en.html`: Chinese and English provenance pages.
- `data/i18n.json`: complete Chinese and English interface text.
- `data/voices.json`: full voice catalog, sample scripts, pinned upstream revisions and relative audio paths.
- `site/`: deployable pages and 157 MP3 samples; `index.html` is Chinese and `en.html` is English.
- `scripts/build.py`: generates both gallery pages and distribution tables.
- `scripts/validate.py`: checks completeness, ordering, audio and public content; validates every audio file when ffprobe is available.

### Deployment

`.github/workflows/pages.yml` validates and publishes `site/` through GitHub Actions. It supports manual runs and runs when main is updated. Set the repository's Pages source to GitHub Actions.

### Models & licensing

Kokoro v1.0 provides 54 voices; Kokoro v1.1-zh provides 103. Samples were generated locally with Kokoro 0.9.4 at speed 1.0; web audio is encoded as 128 kbps MP3. Sample scripts were written for this project. No user recordings are included.

This is an independent community project, not an official Kokoro website. It is not affiliated with or endorsed by the model authors. Gallery code and project-authored assets use Apache-2.0. Models, voices and upstream training materials retain their respective licenses and attribution. The canonical Apache license text remains in English. See [LICENSE](LICENSE) and the bilingual [NOTICE.md](NOTICE.md). Model weights, runtime environments and caches are not included in this repository.
