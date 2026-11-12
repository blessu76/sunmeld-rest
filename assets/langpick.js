/* Sunmeld: first visit to "/" -> the visitor's browser language (inlined into the root home page only; build_site fills in the list).
   Order: the language the visitor picked on the site (localStorage "sm-lang") > first match in navigator.languages, read the same
   way as ipe_web_kit.languages.resolve (zh-TW/zh-HK/zh-Hant -> zh-Hant, zh-CN -> skipped, pt-* -> pt-BR, es-* -> es, in -> id)
   > stay on the English root. No server redirect: crawlers see "/" as English. */
(function(){
  var S=/*SUPPORTED*/[];
  function hant(p){
    var s='',g='';
    for(var j=1;j<p.length;j++){
      if(!s&&p[j].length===4&&/^[a-z]+$/.test(p[j]))s=p[j];
      if(!g&&p[j].length===2&&/^[a-z]+$/.test(p[j]))g=p[j];
    }
    return s==='hant'||(!s&&(g==='tw'||g==='hk'||g==='mo'));
  }
  function pick(p){
    var b=p[0],r=b==='in'?'id':b==='zh'?(hant(p)?'zh-hant':''):b==='pt'?'pt-br':b;
    for(var i=0;i<S.length;i++)if(S[i].toLowerCase()===r)return S[i];
    return '';
  }
  try{
    if(location.pathname!=='/')return;
    var to='',saved='';
    try{saved=localStorage.getItem('sm-lang')||''}catch(e){}
    if(S.indexOf(saved)>=0)to=saved;
    else{
      var L=(navigator.languages&&navigator.languages.length)?navigator.languages:[navigator.language||''];
      for(var i=0;i<L.length&&!to;i++){
        var got=pick(String(L[i]||'').toLowerCase().replace(/_/g,'-').split('-'));
        if(got)to=got;
      }
    }
    if(to&&to!=='en')location.replace('/'+to+'/'+location.search+location.hash);
  }catch(e){}
})();
