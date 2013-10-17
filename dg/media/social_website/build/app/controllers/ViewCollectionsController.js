define(["require","app/controllers/DigitalGreenPageController","framework/Util","jquery","libs/external/swfobject/swfobject","libs/external/buttons","app/libs/VideoLikeDataFeed","app/view-controllers/CommentsFeedViewController","libs/NCarousel/NCarousel"],function(e){var t=e("app/controllers/DigitalGreenPageController"),n=e("framework/Util"),r=e("jquery");e("libs/external/swfobject/swfobject"),e("libs/external/buttons");var i=e("app/libs/VideoLikeDataFeed"),s=e("app/view-controllers/CommentsFeedViewController"),o=e("libs/NCarousel/NCarousel"),u=t.extend({constructor:function(e,t){this.base(e,t),this._initVideoPlayer(),stLight.options({publisher:"5e0ffe84-d022-4b7d-88e1-a273f081e67e",doNotHash:!1,doNotCopy:!1,hashAddressBar:!1}),this._initVideoStats(),this._getComments()},_initConfig:function(){},_initReferences:function(){this.base();var e=this._references;e.$commentsAreaWrapper=r(".js-comments-feed-wrapper"),e.commentsFeedViewController=new s(e.$commentsAreaWrapper),e.videoLikeDataFeed=new i,e.$likeButton=r(".js-like-button"),e.$commentBox=r("#comment"),e.$commentButton=r(".comment-btn"),e.$videoTarget=r("#video-target");var t=r("#collection-videos-carousel");e.videosCarousel=new o(t,{autoPlay:!1,allowWrapping:!1})},_initEvents:function(){this.base();var e=this._references,t=this._boundFunctions;t.onDataProcessed=this._onDataProcessed.bind(this),e.videoLikeDataFeed.on("dataProcessed",t.onDataProcessed),t.onLikeButtonClick=this._onVideoLikeButtonClick.bind(this),e.$likeButton.on("click",t.onLikeButtonClick),t.onCommentButtonClick=this._onCommentButtonClick.bind(this),e.$commentButton.on("click",t.onCommentButtonClick),t.onCommentLikeButtonClick=this._onCommentLikeButtonClick.bind(this),e.$commentsAreaWrapper.on("click",".js-comment-like-button",t.onCommentLikeButtonClick)},_initState:function(){this.base();var e=this._state;e.videoLiked=!1,e.userID=r("body").data("userId"),e.videoUID=this._references.$videoTarget.data("video-uid"),this._references.videoLikeDataFeed.fetch(e.videoUID,e.userID),e.updateVideoWatchedTimeInterval=undefined,this._references.videosCarousel.moveToSlide(parseInt(($(".video-wrapper").attr("data-videoid")-1)/5),{stopAutoPlay:!1})},_initVideoStats:function(){var e=r(".js-stat-bar-wrapper"),t,i,s,o,u=0,a=e.length;for(;u<a;u++){var f=e.eq(u);t=f.find(".js-stat-bar");var l=t.data("leftValue"),c=t.data("rightValue");i=f.find(".js-left-value"),s=f.find(".js-right-value"),i.html(n.integerCommaFormat(l)),s.html(n.integerCommaFormat(c)),o=f.find(".js-stat-indicator"),o.animate({width:l*100/(l+c)+"%"},2e3)}},_initVideoPlayer:function(){var e=this._references.$videoTarget.data("videoId"),t={allowScriptAccess:"always"},n={id:"video-player"};swfobject.embedSWF("http://www.youtube.com/v/"+e+"?enablejsapi=1&playerapiid=ytplayer&version=3","video-target","703","395","8",null,null,t,n),window.onYouTubePlayerReady=this._onYouTubePlayerReady.bind(this)},_onYouTubePlayerReady:function(){window.onYouTubePlayerReady=undefined;var e=r("#video-player").get(0);this._references.videoPlayer=e,window.onYouTubePlayerStateChange=this._onYouTubePlayerStateChange.bind(this),e.addEventListener("onStateChange","onYouTubePlayerStateChange");var t=r(".video-wrapper").attr("data-videoid");t!=1&&e.playVideo()},_onYouTubePlayerStateChange:function(e){switch(e){case 0:var t=r(".now-playing").closest("li"),n=t.next();if(n.length==0){var i=t.closest("ul").closest("li").next();i.length==0&&(i=t.closest("ul").closest("li").closest("ul").find("li:first")),n=i.find("ul > li:first-child")}window.location.href=n.find(".vidDrawer-image a").attr("href");case 2:this._stopUpdateInterval(),this._updateVideoWatchedTime();break;case 1:this._startUpdateInterval()}},_startUpdateInterval:function(){this._stopUpdateInterval(),this._state.updateVideoWatchedTimeInterval=setInterval(this._updateVideoWatchedTime.bind(this),this._config.updateVideoWatchedTimeDelay)},_stopUpdateInterval:function(){clearInterval(this._state.updateVideoWatchedTimeInterval),this._state.updateVideoWatchedTimeInterval=null},_updateVideoWatchedTime:function(){var e=this._state.videoUID,t=this._state.userID},_getComments:function(){this._references.commentsFeedViewController.getComments()},_onDataProcessed:function(e){this._state.videoLiked=e[0].liked,this._state.videoLiked&&this._references.$likeButton.addClass("liked")},_onVideoLikeButtonClick:function(e){e.preventDefault();if(this._state.videoLiked)return;var t=r(e.currentTarget),n=this._state.videoUID,i=this._state.userID;if(n==undefined||i==undefined)throw new Error("ViewCollectionsController._onVideoLikeButtonClick: videoUID and userID are required parameters");this._references.videoLikeDataFeed.fetch(n,i,function(){},"POST")},_onCommentButtonClick:function(e){e.preventDefault();var t=r(e.currentTarget),n=this._state.videoUID,i=this._state.userID,s=this._references.$commentBox.val();if(n==undefined||i==undefined||s==undefined)throw new Error("ViewCollectionsController._onCommentButtonClick: videoUID ,userID, text are required parameters");this._references.commentsFeedViewController.addNewComment(n,i,s),this._references.$commentBox.val("")},_onCommentLikeButtonClick:function(e){e.preventDefault();if(this._state.videoLiked)return;var t=r(e.currentTarget),n=t.data("commentUid"),i=t.data("commentLiked"),s=this._state.userID;if(n==undefined||s==undefined||i==undefined)throw new Error("ViewCollectionsController._onVideoLikeButtonClick: commentUID, userID, and commentLiked are required parameters");var o=i!="1";this._references.commentLikeDataFeed.fetch(n,s,o,this._onCommentLikedCallback.bind(this,t,o))},_onVideoLikedCallback:function(){var e=this._references.videoLikeDataFeed.getResponseStatus();e.success&&(this._references.$likeButton.addClass("liked"),this._state.videoLiked=!0)},_onCommentLikedCallback:function(e,t,r){var i=this._references.commentLikeDataFeed.getResponseStatus();if(i.success)if(t){e.addClass("liked").data("commentLiked",t?"1":"0");var s=r.likedCount||0;e.find(".js-like-count").html(n.integerCommaFormat(s)),e.find(".js-like-label").html(s!=1?"Likes":"Like")}else e.removeClass("liked").data("commentLiked",t?"1":"0")},destroy:function(){this.base()}});return u});