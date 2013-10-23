define(["framework/LifecycleBase"],function(e){var t=e.extend({_events:null,_eventQueue:null,_queueingEvents:!1,constructor:function(){this._constructor()},_constructor:function(){this._events={},this._eventQueue=[]},_checkConstructed:function(){this._events===null&&this._constructor()},setEventQueueing:function(e){this._checkConstructed(),this._queueingEvents=!!e},triggerFlushQueue:function(){this._checkConstructed();if(!this._eventQueue.length)return;var e=this._queueingEvents;this._queueingEvents=!1;for(var t=0,n=this._eventQueue.length;t<n;t++){var r=this._eventQueue[t],i=r.args;i.unshift(r.id),this.trigger.apply(this,i)}this._eventQueue.splice(0),this._queueingEvents=e},on:function(e,t){this._checkConstructed();var n=this._events;return e in n==0&&(n[e]=[]),n[e].push(t),this},off:function(e,t){this._checkConstructed();var n=this._events;if(e in n==0)return!1;var r=!1;for(var i=0,s=n[e].length;i<s;i++)n[e][i]==t&&(r=!0,n[e].splice(i,1));return r},clearAllEvents:function(){this._checkConstructed();var e=this._events;for(var t in e)e[t]=null,delete e[t]},trigger:function(e){this._checkConstructed();var t=Array.prototype.slice.call(arguments,1);if(this._queueingEvents){this._eventQueue.push({id:e,args:t});return}var n=this._events;if(e in n==0||n[e].length==0)return!1;var r=n[e],i=!1;for(var s=0,o=r.length;s<o;s++){var u=r[s];if(typeof u!="function")continue;t.length?r[s].apply(this,t):r[s].call(this),i=!0}return i},destroy:function(){this.clearAllEvents(),this.base()}});return t});