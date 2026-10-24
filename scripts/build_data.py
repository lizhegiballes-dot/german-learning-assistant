"""Build attributed open-data dictionaries; never reads a personal learning DB."""
import argparse,gzip,hashlib,json,re,xml.etree.ElementTree as ET
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--gemet',type=Path,required=True);p.add_argument('--handedict',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
R='{http://www.w3.org/1999/02/22-rdf-syntax-ns#}';S='{http://www.w3.org/2004/02/skos/core#}';X='{http://www.w3.org/XML/1998/namespace}'
raw=a.gemet.read_bytes();rows=[]
for node in ET.fromstring(gzip.decompress(raw)):
 uri=node.get(R+'about','')
 if not uri.startswith('concept/'):continue
 labels={};aliases=[]
 for child in node:
  lang=child.get(X+'lang','');text=' '.join(''.join(child.itertext()).split())
  if child.tag==S+'prefLabel' and lang in ('de','en','zh-CN'):labels[lang]=text
  if child.tag==S+'altLabel' and lang=='de' and text:aliases.append(text)
 if labels.get('de') and (labels.get('en') or labels.get('zh-CN')):rows.append({'id':uri.split('/')[1],'de':labels['de'],'en':labels.get('en',''),'zh':labels.get('zh-CN',''),'aliases':sorted(set(aliases))})
rows.sort(key=lambda r:int(r['id']));meta={'source':'GEMET','version':'4.2.3','url':'https://www.eionet.europa.eu/gemet/latest/gemet.rdf.gz','sha256':hashlib.sha256(raw).hexdigest(),'license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','attribution':'European Environment Agency / Eionet, GEMET','changes':'Extracted German, English and Simplified Chinese labels and German alternatives; definitions and other languages omitted.'}
(a.out/'gemet.json').write_text(json.dumps({'meta':meta,'entries':rows},ensure_ascii=False,separators=(',',':')),encoding='utf8')
source=a.handedict.read_bytes();tuples=set();header=[]
for line in source.decode('utf-8-sig').splitlines():
 if line.startswith('#'):header.append(line);continue
 m=re.match(r'\S+ (\S+) \[[^\]]+\] /(.+)/$',line)
 if not m:continue
 cn,body=m.groups()
 for sense in body.split('/'):
  kind=re.search(r'\((S|V|Adj|Adv)(?:[, )])',sense);pos={'S':'n','V':'v','Adj':'adj','Adv':'adv'}.get(kind[1] if kind else '','other')
  context='; '.join(re.findall(r'\(([^)]*)\)',sense))[:180]
  for word in re.sub(r'\([^)]*\)','',sense).split(','):
   word=' '.join(word.split())
   if word and len(word)<=120 and not re.search(r'[\u3400-\u9fff{}=<>]',word):tuples.add((word,pos,cn,context))
meta={'source':'HanDeDict','url':'https://github.com/gugray/HanDeDict','sha256':hashlib.sha256(source).hexdigest(),'license':'CC BY-SA 3.0','license_url':'https://creativecommons.org/licenses/by-sa/3.0/','attribution':'HanDeDict contributors; published by Gábor L Ugray; original dictionary supported by Chinesisch-Deutsche Gesellschaft e.V. Hamburg, Michael Klaus Engel and Jan Hefti','changes':'Reverse exact German labels into Chinese reference matches. Parenthetic context retained; no substring or compound-word guessing.'}
(a.out/'handedict.json').write_text(json.dumps({'meta':meta,'entries':sorted(tuples)},ensure_ascii=False,separators=(',',':')),encoding='utf8');(a.out/'handedict-attribution.txt').write_text('\n'.join(header)+'\n',encoding='utf8')
print(json.dumps({'gemet':len(rows),'handedict':len(tuples),'files':{f.name:f.stat().st_size for f in a.out.iterdir()}},ensure_ascii=True))
