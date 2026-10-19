# Provenance and attribution

Kokoro Voice Gallery is an independent community project by purryc / shinoyan.
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
