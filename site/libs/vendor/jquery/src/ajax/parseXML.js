define(["../core"],function(e){return e.parseXML=function(r){var n,t;if(!r||"string"!=typeof r)return null;try{window.DOMParser?(t=new DOMParser,n=t.parseFromString(r,"text/xml")):(n=new ActiveXObject("Microsoft.XMLDOM"),n.async="false",n.loadXML(r))}catch(a){n=void 0}return n&&n.documentElement&&!n.getElementsByTagName("parsererror").length||e.error("Invalid XML: "+r),n},e.parseXML});