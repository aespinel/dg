(function(e,t){function f(e,t){this.$target=e,this.selector=t.selector,this.data=t.data,this.moved=!1,this.namespace=i+o++,this.startX=0,this.startY=0,this.startTime=0,this.touchStartCount=0,this.setupHandlers().reset().enable()}t.support.touch="ontouchstart"in window||window.DocumentTouch&&e instanceof DocumentTouch;var n=300,r=10,i=".__tap-helper",s="tap",o=0,u=["clientX","clientY","screenX","screenY","pageX","pageY"],a=function(e,n){var r=0,i=u.length,o=e.originalEvent.changedTouches[0],a=t.Event(s,e);a.type=s,a.data=n;for(;r<i;r++)a[u[r]]=o[u[r]];return a};f.prototype={setupHandlers:function(){return this.onTouchStart=this._onTouchStart.bind(this),this.onTouchMove=this._onTouchMove.bind(this),this.onTouchEnd=this._onTouchEnd.bind(this),this.onTouchCancel=this._onTouchCancel.bind(this),this.onClick=this._onClick.bind(this),this},enable:function(){return t.support.touch?this.$target.on("touchstart"+this.namespace,this.selector,this.onTouchStart):this.$target.on("click"+this.namespace,this.selector,this.onClick),this},disable:function(){return t.support.touch?this.$target.off("touchstart"+this.namespace,this.selector,this.onTouchStart):this.$target.off("click"+this.namespace,this.selector,this.onClick),this},reset:function(){return this.moved=!1,this.startX=0,this.startY=0,this.startTime=0,this.touchStartCount=0,this},destroy:function(){return this.onTouchCancel(),this.disable()},_onTouchStart:function(e){this.touchStartCount=e.originalEvent.touches.length;if(this.touchStartCount>1)return;this.$element=t(e.target),this.moved=!1,this.startX=e.originalEvent.touches[0].clientX,this.startY=e.originalEvent.touches[0].clientY,this.startTime=Date.now(),this.$target.on("touchmove"+this.namespace,this.selector,this.onTouchMove).on("touchend"+this.namespace,this.selector,this.onTouchEnd).on("touchcancel"+this.namespace,this.selector,this.onTouchCancel)},_onTouchMove:function(e){var t=e.originalEvent.touches[0].clientX,n=e.originalEvent.touches[0].clientY;if(Math.abs(t-this.startX)>r||Math.abs(n-this.startY)>r)this.moved=!0},_onTouchEnd:function(e){if(!this.touchStartCount||e.originalEvent.touches.length>0)return;if(this.touchStartCount>1)return;var t=e.target.tagName,r=e.target==e.currentTarget||t!="A";!e.originalEvent.firstTap&&!this.moved&&Date.now()-this.startTime<n&&r&&(e.originalEvent.firstTap=!0,this.$target.trigger(a(e,this.data))),this.onTouchCancel()},_onTouchCancel:function(){this.reset().$target.off("touchmove"+this.namespace,this.selector,this.onTouchMove).off("touchend"+this.namespace,this.selector,this.onTouchEnd).off("touchcancel"+this.namespace,this.selector,this.onTouchCancel)},_onClick:function(e){!e.isTrigger&&!e.originalEvent.firstTap&&(e.originalEvent.firstTap=!0,e.type="tap",this.$target.trigger(e))}},t.event.special[s]={add:function(e){e.tap=new f(t(this),e)},remove:function(e){e.tap&&e.tap.destroy&&e.tap.destroy()}}})(document,jQuery);