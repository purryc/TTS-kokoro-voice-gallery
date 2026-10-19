"""Build the standalone static gallery using only Python's standard library."""
from collections import Counter
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = [('zh','中文'),('en','英语'),('es','西班牙语'),('fr','法语'),('hi','印地语'),('it','意大利语'),('ja','日语'),('pt','葡萄牙语')]

def main():
    voices = json.loads((ROOT/'data/voices.json').read_text())
    translations = json.loads((ROOT/'data/i18n.json').read_text())
    rows=[]
    for lang,name in LANGUAGES:
        counts=Counter(v['gender'] for v in voices if v['lang']==lang)
        rows.append(f'<tr><th scope="row" data-i18n="{lang}">__{lang}__</th><td>{counts["女声"]}</td><td>{counts["男声"]}</td><td>{sum(counts.values())}</td></tr>')
    total=Counter(v['gender'] for v in voices)
    table='<table data-i18n-aria="distributionLabel" aria-label="__distributionLabel__"><thead><tr>'+''.join(f'<th scope="col" data-i18n="{key}">__{key}__</th>' for key in ['language','female','male','total'])+'</tr></thead><tbody>'+''.join(rows)+f'</tbody><tfoot><tr><th scope="row" data-i18n="total">__total__</th><td>{total["女声"]}</td><td>{total["男声"]}</td><td>{len(voices)}</td></tr></tfoot></table>'
    template=(ROOT/'templates/index.html').read_text()
    assert template.count('__VOICE_DATA__')==1 and template.count('__DISTRIBUTION__')==1
    for locale, filename in [('zh','index.html'),('en','en.html')]:
        values={**translations[locale], 'locale':locale, 'zhCurrent':'page' if locale=='zh' else 'false', 'enCurrent':'page' if locale=='en' else 'false', 'aboutFile':'about-en.html' if locale=='en' else 'about.html', 'pageUrl':'https://purryc.github.io/kokoro-voice-gallery/'+('en.html' if locale=='en' else '')}
        page=template.replace('__DISTRIBUTION__',table)
        page=re.sub(r'__([a-zA-Z]+)__', lambda m:html.escape(values[m[1]],quote=True) if m[1] in values else m[0], page)
        page=page.replace('__VOICE_DATA__',json.dumps(voices,ensure_ascii=False).replace('</','<\\/')).replace('__I18N_DATA__',json.dumps(translations,ensure_ascii=False).replace('</','<\\/'))
        (ROOT/'site'/filename).write_text(page)
    for filename in ['about.html','about-en.html']:
        (ROOT/'site'/filename).write_bytes((ROOT/'templates'/filename).read_bytes())
    (ROOT/'site/voices.json').write_text(json.dumps(voices,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'site/.nojekyll').touch()
    for name in ['LICENSE','NOTICE.md']:
        (ROOT/'site'/name).write_bytes((ROOT/name).read_bytes())
    print(f'Built {len(voices)} voices: {total["女声"]} female, {total["男声"]} male')

if __name__=='__main__':main()
