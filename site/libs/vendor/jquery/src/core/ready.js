define(["../core","../core/init","../deferred"],function(e){function t(){document.addEventListener?(document.removeEventListener("DOMContentLoaded",n,!1),window.removeEventListener("load",n,!1)):(document.detachEvent("onreadystatechange",n),window.detachEvent("onload",n))}function n(){(document.addEventListener||"load"===event.type||"complete"===document.readyState)&&(t(),e.ready())}var d;e.fn.ready=function(t){return e.ready.promise().done(t),this},e.extend({isReady:!1,readyWait:1,holdReady:function(t){t?e.readyWait++:e.ready(!0)},ready:function(t){if(t===!0?!--e.readyWait:!e.isReady){if(!document.body)return setTimeout(e.ready);e.isReady=!0,t!==!0&&--e.readyWait>0||(d.resolveWith(document,[e]),e.fn.triggerHandler&&(e(document).triggerHandler("ready"),e(document).off("ready")))}}}),e.ready.promise=function(o){if(!d)if(d=e.Deferred(),"complete"===document.readyState)setTimeout(e.ready);else if(document.addEventListener)document.addEventListener("DOMContentLoaded",n,!1),window.addEventListener("load",n,!1);else{document.attachEvent("onreadystatechange",n),window.attachEvent("onload",n);var a=!1;try{a=null==window.frameElement&&document.documentElement}catch(r){}a&&a.doScroll&&!function i(){if(!e.isReady){try{a.doScroll("left")}catch(n){return setTimeout(i,50)}t(),e.ready()}}()}return d.promise(o)}});