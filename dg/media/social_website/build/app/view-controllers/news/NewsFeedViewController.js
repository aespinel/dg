define(["require","framework/controllers/Controller","framework/ViewRenderer","framework/Util","jquery","libs/NCarousel/NCarousel","app/libs/NewsDataFeed","text!app/views/news/newsItem.html"],function(e){var t=e("framework/controllers/Controller"),n=e("framework/ViewRenderer"),r=e("framework/Util"),i=e("jquery"),s=e("libs/NCarousel/NCarousel"),o=e("app/libs/NewsDataFeed"),u=e("text!app/views/news/newsItem.html"),a=t.extend({constructor:function(e){return this.base(e),this},_initConfig:function(){this.base()},_initReferences:function(e){this.base();var t=this._references;t.dataFeed=new o,t.$newsItemsWrapper=e,t.$newsItemsContainer=e.find(".js-news-feed-container"),t.$newsFeedShowMoreButton=e.find(".js-news-feed-show-more-btn")},_initState:function(){this.base();var e=this._state;e.currentPageNumber=0,e.newsItemsPerPage=10,e.currentCount=0},_initEvents:function(){this.base();var e=this._boundFunctions,t=this._references;e.onDataProcessed=this._onDataProcessed.bind(this),t.dataFeed.on("dataProcessed",e.onDataProcessed),e.onShowMoreClick=this._onShowMoreClick.bind(this),t.$newsFeedShowMoreButton.on("click",e.onShowMoreClick)},setNewsItemsPerPage:function(e){return this._state.newsItemsPerPage=e,this},getNewsItemsPerPage:function(){return this._state.newsItemsPerPage},setCurrentPageNumber:function(e){return this._state.currentPageNumber=e,this},getCurrentPageNumber:function(){return this._state.currentPageNumber},getNewsItems:function(e,t){e==undefined?e=this.getCurrentPageNumber():this.setCurrentPageNumber(e),t==undefined?t=this.getNewsItemsPerPage():this.setNewsItemsPerPage(t);var n=this._references.dataFeed;n.setInputParam("offset",e,!0),n.setInputParam("limit",t,!0);var r=n.getNewsItems(),i=n.getTotalCount();if(r==0)return!1;this._updateNewsFeedDisplay(r,i)},_onDataProcessed:function(){this.getNewsItems()},_updateNewsFeedDisplay:function(e,t){this._prepareData(e),this._renderNewsItems(e);var n={totalCount:t,addedCount:e.length};this.trigger("newsFeedUpdated",n)},_renderNewsItems:function(e){var t={activities:e};n.renderAppend(this._references.$newsItemsContainer,u,t),this._initCarousels()},_initCarousels:function(){var e=this._references.$newsItemsContainer.find(".js-carousel-wrapper"),t=0,n=e.length;for(;t<n;t++)new s(e.eq(t),{autoPlay:!1,allowWrapping:!1})},_prepareData:function(e){var t=0,n=e.length;for(;t<n;t++){var i=e[t];i._hasImages=i.images&&i.images.length!=0,i.images&&i.images.length>4&&(i.images=i.images.splice(0,4));if(i.collection&&i.collection.videos){var s=i.collection.videos,o={likes:0,views:0,adoptions:0,time:0},u=[],a=[],f=0,l=s.length;for(;f<l;f++){var c=s[f];o.likes+=c.offlineLikes+c.onlineLikes,o.views+=c.offlineViews+c.onlineViews,o.adoptions+=c.adoptions,o.totalDuration+=c.duration,a.push(c);if(f>0&&(f+1)%4==0||f==l-1)u.push({videos:a}),a=[]}i.collection._carouselSlides=u,o.likes=r.integerCommaFormat(o.likes),o.views=r.integerCommaFormat(o.views),o.adoptions=r.integerCommaFormat(o.adoptions),o.totalDuration=r.secondsToHMSFormat(o.totalDuration),i.collection._collectionStats=o}}},updateTotalCount:function(e){this._state.totalCount=e},addToCurrentCount:function(e){this._state.currentCount+=e},updateNewsItemPaginationDisplay:function(){this._state.currentCount>=this._state.totalCount&&this._references.$newsFeedShowMoreButton.hide()},_onShowMoreClick:function(e){e.preventDefault(),e.stopPropagation(),this.getNewsItems(this.getCurrentPageNumber()+1)},setInputParam:function(e,t,n){if(!this._references.dataFeed.setInputParam(e,t,n))return},destroy:function(){this.base()}});return a});