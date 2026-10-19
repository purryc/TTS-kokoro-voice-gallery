# 来源与署名 / Provenance and attribution

[中文](#中文说明) · [English](#english)

## English

TTS-kokoro-voice-gallery is an independent community project by purryc / shinoyan.
It is not affiliated with or endorsed by hexgrad or the Kokoro model authors.

## Models and voice presets

Audio demos were generated locally with Kokoro 0.9.4, speed 1.0, 24 kHz mono,
using the following Apache-2.0 licensed models. This repository contains generated
audio samples, not model weights or copies of voice tensors.

- Kokoro inference code: https://github.com/hexgrad/kokoro
- Kokoro v1.0: https://huggingface.co/hexgrad/Kokoro-82M
  - revision: f3ff3571791e39611d31c381e3a41a3af07b4987
  - 54 voice presets
- Kokoro v1.1-zh: https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh
  - revision: 01e7505bd6a7a2ac4975463114c3a7650a9f7218
  - 103 voice presets

Both catalogs are combined without renaming upstream voice IDs. Display row
numbers are gallery indices, not new official voice IDs. Female/male labels
follow upstream preset identifiers; they are not demographic claims about users.

WAV originals were transcoded to 128 kbps MP3 for web playback. Demo scripts and
source revisions are included in data/voices.json. Sample quality has not been
ranked. This site does not offer voice cloning or live speech synthesis.

## Upstream dataset attribution

The v1.0 model card identifies Koniwa TNC material under CC BY 3.0 and SIWIS
under CC BY 4.0. These are upstream training-source notices, not assertions that
the generated demos are source recordings. Original audio recordings are not
included in this repository.

- Model card: https://huggingface.co/hexgrad/Kokoro-82M
- Voice source table: https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- Koniwa: https://github.com/koniwa/koniwa
- gongitsune: https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__gongitsune.txt
- nezuminoyomeiri: https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__nezuminoyomeiri.txt
- tebukurowokaini: https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__tebukurowokaini.txt
- kumonoito: https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__kumonoito.txt
- SIWIS: https://datashare.ed.ac.uk/handle/10283/2353
- CC BY 3.0: https://creativecommons.org/licenses/by/3.0/
- CC BY 4.0: https://creativecommons.org/licenses/by/4.0/

The v1.1-zh model card credits the Chinese training data to LongMaoData:
https://www.longmaosoft.com/

## Project license

The gallery code and project-authored assets are distributed under Apache-2.0;
see LICENSE. Upstream models and training materials retain their own licenses
and attribution. No rights to the Kokoro name or third-party marks are claimed.

---

## 中文说明

TTS-kokoro-voice-gallery 是由 purryc / shinoyan 制作的独立社区项目，与 hexgrad 或 Kokoro 模型作者无隶属或背书关系。

### 模型与预设音色

样音通过 Kokoro 0.9.4 在本地生成，语速 1.0、24 kHz 单声道，使用以下采用 Apache-2.0 许可的模型。本仓库包含生成的样音，不包含模型权重或音色张量副本。

- Kokoro 推理代码：https://github.com/hexgrad/kokoro
- Kokoro v1.0：https://huggingface.co/hexgrad/Kokoro-82M
  - 固定版本：f3ff3571791e39611d31c381e3a41a3af07b4987
  - 54 个预设音色
- Kokoro v1.1-zh：https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh
  - 固定版本：01e7505bd6a7a2ac4975463114c3a7650a9f7218
  - 103 个预设音色

合并两个目录时保留上游音色 ID。列表序号是本站索引，不是新的官方音色 ID。女声、男声标签沿用上游预设标识，并非对用户人口属性的判断。

原始 WAV 转码为 128 kbps MP3 供网页播放。试听文案及模型来源版本记录在 `data/voices.json`。本站没有对音质作主观排名，不提供声音克隆或实时语音合成。

### 上游数据集署名

v1.0 模型卡列出 Koniwa TNC 素材采用 CC BY 3.0，SIWIS 采用 CC BY 4.0。以下是上游训练来源的署名说明，不意味着生成的样音就是源录音。本仓库不包含原始录音。

- 模型卡：https://huggingface.co/hexgrad/Kokoro-82M
- 音色来源表：https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- Koniwa：https://github.com/koniwa/koniwa
- gongitsune：https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__gongitsune.txt
- nezuminoyomeiri：https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__nezuminoyomeiri.txt
- tebukurowokaini：https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__tebukurowokaini.txt
- kumonoito：https://github.com/koniwa/koniwa/blob/master/source/tnc/tnc__kumonoito.txt
- SIWIS：https://datashare.ed.ac.uk/handle/10283/2353
- CC BY 3.0：https://creativecommons.org/licenses/by/3.0/
- CC BY 4.0：https://creativecommons.org/licenses/by/4.0/

v1.1-zh 模型卡将中文训练数据署名给 LongMaoData：https://www.longmaosoft.com/

### 项目许可

试听页代码及项目原创资产采用 Apache-2.0，详见 [LICENSE](LICENSE)。上游模型与训练素材保留各自许可和署名。本项目不主张对 Kokoro 名称或第三方商标拥有权利。Apache 许可证保留英文正式文本，本说明用于解释项目范围与来源。
