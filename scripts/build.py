"""Build the standalone static gallery using only Python's standard library."""
from collections import Counter
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = [('zh','中文'),('en','英语'),('es','西班牙语'),('fr','法语'),('hi','印地语'),('it','意大利语'),('ja','日语'),('pt','葡萄牙语')]

def main():
    voices = json.loads((ROOT/'data/voices.json').read_text())
    rows=[]
    for lang,name in LANGUAGES:
        counts=Counter(v['gender'] for v in voices if v['lang']==lang)
        rows.append(f'<tr><th scope="row">{name}</th><td>{counts["女声"]}</td><td>{counts["男声"]}</td><td>{sum(counts.values())}</td></tr>')
    total=Counter(v['gender'] for v in voices)
    table='<table aria-label="各语言女声男声数量"><thead><tr><th scope="col">语言</th><th scope="col">女声</th><th scope="col">男声</th><th scope="col">合计</th></tr></thead><tbody>'+''.join(rows)+f'</tbody><tfoot><tr><th scope="row">合计</th><td>{total["女声"]}</td><td>{total["男声"]}</td><td>{len(voices)}</td></tr></tfoot></table>'
    template=(ROOT/'templates/index.html').read_text()
    assert template.count('__VOICE_DATA__')==1 and template.count('__DISTRIBUTION__')==1
    page=template.replace('__VOICE_DATA__',json.dumps(voices,ensure_ascii=False).replace('</','<\\/')).replace('__DISTRIBUTION__',table)
    (ROOT/'site/index.html').write_text(page)
    (ROOT/'site/voices.json').write_text(json.dumps(voices,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'site/.nojekyll').touch()
    for name in ['LICENSE','NOTICE.md']:
        (ROOT/'site'/name).write_bytes((ROOT/name).read_bytes())
    print(f'Built {len(voices)} voices: {total["女声"]} female, {total["男声"]} male')

if __name__=='__main__':main()
