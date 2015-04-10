define(["./core","./traversing/var/rneedsContext","./core/init","./traversing/findFilter","./selector"],function(n,t){function e(n,t){do n=n[t];while(n&&1!==n.nodeType);return n}var i=/^(?:parents|prev(?:Until|All))/,r={children:!0,contents:!0,next:!0,prev:!0};return n.extend({dir:function(t,e,i){for(var r=[],o=t[e];o&&9!==o.nodeType&&(void 0===i||1!==o.nodeType||!n(o).is(i));)1===o.nodeType&&r.push(o),o=o[e];return r},sibling:function(n,t){for(var e=[];n;n=n.nextSibling)1===n.nodeType&&n!==t&&e.push(n);return e}}),n.fn.extend({has:function(t){var e,i=n(t,this),r=i.length;return this.filter(function(){for(e=0;r>e;e++)if(n.contains(this,i[e]))return!0})},closest:function(e,i){for(var r,o=0,u=this.length,s=[],c=t.test(e)||"string"!=typeof e?n(e,i||this.context):0;u>o;o++)for(r=this[o];r&&r!==i;r=r.parentNode)if(r.nodeType<11&&(c?c.index(r)>-1:1===r.nodeType&&n.find.matchesSelector(r,e))){s.push(r);break}return this.pushStack(s.length>1?n.unique(s):s)},index:function(t){return t?"string"==typeof t?n.inArray(this[0],n(t)):n.inArray(t.jquery?t[0]:t,this):this[0]&&this[0].parentNode?this.first().prevAll().length:-1},add:function(t,e){return this.pushStack(n.unique(n.merge(this.get(),n(t,e))))},addBack:function(n){return this.add(null==n?this.prevObject:this.prevObject.filter(n))}}),n.each({parent:function(n){var t=n.parentNode;return t&&11!==t.nodeType?t:null},parents:function(t){return n.dir(t,"parentNode")},parentsUntil:function(t,e,i){return n.dir(t,"parentNode",i)},next:function(n){return e(n,"nextSibling")},prev:function(n){return e(n,"previousSibling")},nextAll:function(t){return n.dir(t,"nextSibling")},prevAll:function(t){return n.dir(t,"previousSibling")},nextUntil:function(t,e,i){return n.dir(t,"nextSibling",i)},prevUntil:function(t,e,i){return n.dir(t,"previousSibling",i)},siblings:function(t){return n.sibling((t.parentNode||{}).firstChild,t)},children:function(t){return n.sibling(t.firstChild)},contents:function(t){return n.nodeName(t,"iframe")?t.contentDocument||t.contentWindow.document:n.merge([],t.childNodes)}},function(t,e){n.fn[t]=function(o,u){var s=n.map(this,e,o);return"Until"!==t.slice(-5)&&(u=o),u&&"string"==typeof u&&(s=n.filter(u,s)),this.length>1&&(r[t]||(s=n.unique(s)),i.test(t)&&(s=s.reverse())),this.pushStack(s)}}),n});