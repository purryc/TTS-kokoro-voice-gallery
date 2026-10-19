"""Validate public artifacts and the full 157-voice inventory."""
from collections import Counter
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LANG_ORDER={'zh':0,'en':1,'es':2,'fr':3,'hi':4,'it':5,'ja':6,'pt':7}
def key(v):
    return (v['gender']!='女声',LANG_ORDER[v['lang']],[int(x) if x.isdigit() else x for x in re.split(r'(\d+)',v['id'])])

def main():
    voices=json.loads((ROOT/'data/voices.json').read_text())
    assert len(voices)==len({v['id'] for v in voices})==157
    assert voices==sorted(voices,key=key)
    assert [v['sequence'] for v in voices]==list(range(1,158))
    assert Counter(v['gender'] for v in voices)=={'女声':87,'男声':70}
    assert Counter(v['lang'] for v in voices)=={'zh':108,'en':31,'es':3,'fr':1,'hi':4,'it':2,'ja':5,'pt':3}
    page=(ROOT/'site/index.html').read_text()
    embedded=json.loads(page.split('const voices = ',1)[1].split(';\nconst playIcon',1)[0])
    assert embedded==voices
    assert json.loads((ROOT/'site/voices.json').read_text())==voices
    assert '__VOICE_DATA__' not in page and '__DISTRIBUTION__' not in page
    assert '独立社区试听项目' in page
    translations=json.loads((ROOT/'data/i18n.json').read_text())
    assert translations['zh'].keys()==translations['en'].keys()
    for translation_key in translations['zh']:
        assert translations['zh'][translation_key] and translations['en'][translation_key]
        assert re.findall(r'\{\w+\}',translations['zh'][translation_key])==re.findall(r'\{\w+\}',translations['en'][translation_key])
    for filename,locale in [('index.html','zh'),('en.html','en')]:
        localized=(ROOT/'site'/filename).read_text()
        assert not re.search(r'__[A-Za-z_]+__',localized),filename
        assert f'<html lang="{translations[locale]["htmlLang"]}">' in localized
        assert json.loads(localized.split('const voices = ',1)[1].split(';\nconst playIcon',1)[0])==voices
        assert translations[locale]['heading'] in localized.split('<script>')[0]
        assert set(re.findall(r'data-i18n(?:-aria|-placeholder)?="([^"]+)"',localized))<=translations[locale].keys()
    for filename,lang in [('about.html','zh-CN'),('about-en.html','en')]:
        localized=(ROOT/'site'/filename).read_text()
        assert f'<html lang="{lang}">' in localized
        assert (ROOT/'templates'/filename).read_text()==localized
    for filename in ['README.md','NOTICE.md']:
        doc=(ROOT/filename).read_text()
        assert '## 中文说明' in doc and '## English' in doc
    total=0
    for v in voices:
        path=ROOT/'site'/v['file']
        assert re.fullmatch(r'audio/[a-z]+_[a-z0-9]+\.mp3',v['file'])
        assert path.is_file() and path.stat().st_size>1000
        assert len(v['wave'])==64 and v['text']
        total+=path.stat().st_size
        if shutil.which('ffprobe'):
            info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,sample_rate,channels','-of','json',str(path)]))
            assert float(info['format']['duration'])>0 and info['streams'][0]['codec_name']=='mp3'
    assert len(list((ROOT/'site/audio').glob('*.mp3')))==157
    forbidden=[r'/Users/',r'/private/tmp/',r'gh[pousr]_[A-Za-z0-9]{20,}',r'sk-[A-Za-z0-9_-]{20,}',r'hf_[A-Za-z0-9]{25,}']
    for directory in ['site','data','templates','scripts']:
        for p in (ROOT/directory).rglob('*'):
            if p.is_file() and p.suffix in ['.html','.json','.md','.txt']:
                text=p.read_text()
                assert not any(re.search(pattern,text) for pattern in forbidden),f'Private data pattern: {p.relative_to(ROOT)}'
    print(json.dumps({'voices':157,'female':87,'male':70,'audio_bytes':total,'private_content_scan':'passed','sorting':'passed','bilingual_pages_and_docs':'passed'}))

if __name__=='__main__':main()
