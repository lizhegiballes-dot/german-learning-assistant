'use strict';
(() => {
 const flatten=w=>[w.entry.article?[w.entry.article,w.lemma].join(' '):w.lemma,(w.entry.senses.en||[]).map(s=>s.text).join('; '),(w.entry.senses.zh||[]).map(s=>s.text).join('；'),String(w.lookupCount||0),w.firstAt||'',w.lastAt||'',w.note||'',JSON.stringify(w.entry.sources||[])];
 const safe=v=>/^[\s]*[=+@-]/.test(v)?"'"+v:v;
 function csv(words){return '\uFEFF'+[['German','English','Chinese','Lookup count','First lookup','Last lookup','Personal note','Sources and licenses'],...words.map(flatten)].map(row=>row.map(v=>'"'+safe(String(v)).replace(/"/g,'""')+'"').join(',')).join('\r\n');}
 function tsv(words){return '#separator:tab\n#html:false\n#columns:German\tEnglish\tChinese\tLookup count\tFirst lookup\tLast lookup\tPersonal note\tSources and licenses\n'+words.map(flatten).map(row=>row.map(v=>String(v).replace(/[\t\r\n]+/g,' ')).join('\t')).join('\n');}
 globalThis.WortExport={csv,tsv};
})();