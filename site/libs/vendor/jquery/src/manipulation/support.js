define(["../var/support"],function(e){return function(){var n=document.createElement("input"),t=document.createElement("div"),a=document.createDocumentFragment();if(t.innerHTML="  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>",e.leadingWhitespace=3===t.firstChild.nodeType,e.tbody=!t.getElementsByTagName("tbody").length,e.htmlSerialize=!!t.getElementsByTagName("link").length,e.html5Clone="<:nav></:nav>"!==document.createElement("nav").cloneNode(!0).outerHTML,n.type="checkbox",n.checked=!0,a.appendChild(n),e.appendChecked=n.checked,t.innerHTML="<textarea>x</textarea>",e.noCloneChecked=!!t.cloneNode(!0).lastChild.defaultValue,a.appendChild(t),t.innerHTML="<input type='radio' checked='checked' name='t'/>",e.checkClone=t.cloneNode(!0).cloneNode(!0).lastChild.checked,e.noCloneEvent=!0,t.attachEvent&&(t.attachEvent("onclick",function(){e.noCloneEvent=!1}),t.cloneNode(!0).click()),null==e.deleteExpando){e.deleteExpando=!0;try{delete t.test}catch(c){e.deleteExpando=!1}}}(),e});