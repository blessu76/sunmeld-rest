(function(){
  /* an explicit language choice wins over the browser language the root page follows (see langpick.js) */
  var picker=document.querySelector('.langsel');
  if(picker)picker.hidden=false;
  document.addEventListener('change',function(e){
    var s=e.target;
    if(!s||!s.matches||!s.matches('.langsel select'))return;
    var o=s.options[s.selectedIndex];
    try{localStorage.setItem('sm-lang',o.getAttribute('data-lang'))}catch(x){}
    location.href=s.value;
  });
})();
