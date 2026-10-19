# Kokoro Voice Gallery

[打开试听页](https://purryc.github.io/kokoro-voice-gallery/)

157 个 Kokoro 官方预设音色的独立社区试听页。支持试听、搜索、语言与男女声筛选、浏览器本地收藏、MP3 下载。页面只播放预生成样音，无后端、无 API key、无浏览器内语音合成。

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

- `templates/index.html`：页面源模板。
- `data/voices.json`：完整音色数据、试听文案、上游固定版本及相对音频路径。
- `site/`：可部署页面及 157 段 MP3 音频。
- `scripts/build.py`：生成页面与分布表。
- `scripts/validate.py`：完整性、排序、音频与公开内容检查；检测到 ffprobe 时会逐个验证音频。

## 发布

`.github/workflows/pages.yml` 通过 GitHub Actions 验证并发布 `site/`。支持手动运行，也在 main 更新时运行。仓库设置的 Pages 来源需为 GitHub Actions。

## 模型与许可

Kokoro v1.0：54 音色；Kokoro v1.1-zh：103 音色。样音使用 Kokoro 0.9.4 在本地生成，语速 1.0；网页版本为 128 kbps MP3。文案为本项目试听文本，没有用户录音。

本项目为独立社区作品，非 Kokoro 官方网站，与模型作者无隶属或背书关系。
项目代码及项目原创资产采用 Apache-2.0。模型、音色及上游训练素材保留各自许可与署名。详见 [LICENSE](LICENSE) 和 [NOTICE.md](NOTICE.md)。模型权重、运行环境及缓存不包含在本仓库中。
