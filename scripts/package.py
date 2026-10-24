"""Package only the public extension; never walk sibling/private folders."""
import argparse, hashlib, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXT=ROOT/'extension'

def check():
    m=json.loads((EXT/'manifest.json').read_text(encoding='utf-8'))
    assert m['manifest_version']==3 and 'key' not in m
    assert m['host_permissions']==['https://en.wiktionary.org/*']
    assert set(m['permissions'])=={'storage','contextMenus','tts','unlimitedStorage'}
    assert all((EXT/f).is_file() for f in [m['background']['service_worker'],m['action']['default_popup'],m['options_page']])
    for name in ['gemet','handedict']:
        d=json.loads((EXT/'data'/f'{name}.json').read_text(encoding='utf-8'))
        assert d['entries'] and d['meta']['license'] and d['meta']['attribution']
        assert d['meta']['sha256']
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if any(s in {'.git','node_modules','dist','test-results','playwright-report'} for s in rel.parts) or not p.is_file(): continue
        assert p.suffix.lower() not in {'.db','.sqlite','.sqlite3','.apkg','.lnk','.pem','.key'},rel
        assert p.name not in {'.env','config.json','settings.local.json'},rel
        if p.suffix in {'.js','.cjs','.html','.md','.json','.py','.yml'} and 'data' not in rel.parts:
            s=p.read_text(encoding='utf-8')
            assert not re.search(r'[A-Za-z]:[/\\]Users[/\\]',s),rel
            assert not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]+PRIVATE KEY-----',s),rel
            if rel.parts[0]=='extension': assert not any(x in s for x in ['朕的','小皇帝','德语书房','德语书屋']),rel
    print('Public-file, manifest, source attribution and privacy checks passed.')

def package():
    version=json.loads((EXT/'manifest.json').read_text())['version']
    out=ROOT/'dist';out.mkdir(exist_ok=True)
    dest=out/f'wortglide-{version}.zip'
    files={p.relative_to(EXT).as_posix():p for p in EXT.rglob('*') if p.is_file()}
    for name in ['LICENSE','THIRD_PARTY_NOTICES.md','PRIVACY.md','README.md','README.zh-CN.md']:
        files[name]=ROOT/name
    for p in (ROOT/'docs').rglob('*'):
        if p.is_file(): files['docs/'+p.relative_to(ROOT/'docs').as_posix()]=p
    # Reproducible member timestamps and deterministic order.
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,p in sorted(files.items()):
            i=zipfile.ZipInfo(name,date_time=(2026,1,1,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16
            z.writestr(i,p.read_bytes())
    digest=hashlib.sha256(dest.read_bytes()).hexdigest()
    source=out/f'wortglide-source-{version}.zip'
    with zipfile.ZipFile(source,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(ROOT.rglob('*')):
            rel=p.relative_to(ROOT)
            if not p.is_file() or any(s in {'.git','node_modules','dist','test-results','playwright-report','__pycache__'} for s in rel.parts): continue
            i=zipfile.ZipInfo(rel.as_posix(),date_time=(2026,1,1,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16;z.writestr(i,p.read_bytes())
    source_digest=hashlib.sha256(source.read_bytes()).hexdigest()
    (out/'SHA256SUMS.txt').write_text(f'{digest}  {dest.name}\n{source_digest}  {source.name}\n',encoding='ascii')
    print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'sha256':digest},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    check()
    if not args.check: package()
