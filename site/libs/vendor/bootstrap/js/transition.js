/* ========================================================================
 * Bootstrap: transition.js v3.3.1
 * http://getbootstrap.com/javascript/#transitions
 * ========================================================================
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */

+function(n){"use strict";function t(){var n=document.createElement("bootstrap"),t={WebkitTransition:"webkitTransitionEnd",MozTransition:"transitionend",OTransition:"oTransitionEnd otransitionend",transition:"transitionend"};for(var i in t)if(void 0!==n.style[i])return{end:t[i]};return!1}n.fn.emulateTransitionEnd=function(t){var i=!1,r=this;n(this).one("bsTransitionEnd",function(){i=!0});var e=function(){i||n(r).trigger(n.support.transition.end)};return setTimeout(e,t),this},n(function(){n.support.transition=t(),n.support.transition&&(n.event.special.bsTransitionEnd={bindType:n.support.transition.end,delegateType:n.support.transition.end,handle:function(t){return n(t.target).is(this)?t.handleObj.handler.apply(this,arguments):void 0}})})}(jQuery);