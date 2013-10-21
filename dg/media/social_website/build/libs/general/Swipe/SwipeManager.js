define(["require","framework/LifecycleBase","libs/general/Swipe/SwipeListener","jquery"],function(e){var t=e("framework/LifecycleBase"),n=e("libs/general/Swipe/SwipeListener"),r=e("jquery"),i=t.extend({_configuration:{diagonalThreshold:.5},SWIPE_UNITS:{PIXELS:0,PERCENT:1},SWIPE_TYPES:{AUTODETECT:0,LEFT:1,RIGHT:2,UP:3,DOWN:4,UP_LEFT:5,DOWN_LEFT:6,UP_RIGHT:7,DOWN_RIGHT:8},deviceEvents:null,_state:{previousScrollPosition:null,hasTouchEvents:!1},_listeners:[],constructor:function(){this.deviceEvents={};var e=this._state.hasTouchEvents="ontouchend"in document;e?(this.deviceEvents.startEvent="touchstart",this.deviceEvents.moveEvent="touchmove",this.deviceEvents.endEvent="touchend"):(this.deviceEvents.startEvent="mousedown",this.deviceEvents.moveEvent="mousemove",this.deviceEvents.endEvent="mouseup"),this._bindEvents(),this._state.previousScrollPosition={x:window.scrollX,y:window.scrollY}},_bindEvents:function(){r("body").on(this.deviceEvents.moveEvent,this._onSwipeMove.bind(this)).on(this.deviceEvents.endEvent,this._onSwipeEnd.bind(this))},getConfiguration:function(){return this._configuration},addListener:function(e){var t=null;if(e instanceof n)t=e;else{t=this.getListenerByTarget(e);if(t)return t;t=new n(this,e)}return this._listeners.push(t),t},_getListenerIndex:function(e){for(var t=0,n=this._listeners.length;t<n;t++)if(this._listeners[t].matchTarget(e))return t;return!1},_getListenerByIndex:function(e){var t=this._listeners;return t.length==0||e<0||e>=t.length?!1:this._listeners[e]},getListenerByTarget:function(e){return this._getListenerByIndex(this._getListenerIndex(e))},removeListener:function(e){var t=null;while(!1!==(t=this._getListenerIndex(e))){var n=this._getListenerByIndex[t];n&&(currentListener.remove(),this._listeners.splice(t,1))}},removeAllListeners:function(){for(var e=0,t=this._listeners.length;e<t;e++)this._listeners[e].remove();this._listeners.splice(0)},removeSwipeConfiguration:function(e,t){var n=this.getListenerByTarget(e)},_onSwipeMove:function(e){for(var t=0,n=this._listeners.length;t<n;t++)this._listeners[t].triggerEvent("swipeMove",e)},_onSwipeEnd:function(e){for(var t=0,n=this._listeners.length;t<n;t++)this._listeners[t].triggerEvent("swipeEnd",e)},_reverseEnum:function(e,t){for(var n in e)if(e[n]==t)return n;return null},destructor:function(){this.removeAllListeners(),this.base()}});return i});