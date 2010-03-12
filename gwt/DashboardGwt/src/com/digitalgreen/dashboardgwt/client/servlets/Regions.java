package com.digitalgreen.dashboardgwt.client.servlets;

import java.util.HashMap;
import java.util.List;

import com.digitalgreen.dashboardgwt.client.common.ApplicationConstants;
import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.OnlineOfflineCallbacks;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.data.BaseData;
import com.digitalgreen.dashboardgwt.client.data.IndexData;
import com.digitalgreen.dashboardgwt.client.data.LoginData;
import com.digitalgreen.dashboardgwt.client.data.RegionsData;
import com.digitalgreen.dashboardgwt.client.templates.RegionsTemplate;
import com.digitalgreen.dashboardgwt.client.templates.ScreeningsTemplate;
import com.google.gwt.user.client.Cookies;
import com.google.gwt.user.client.Window;
import com.google.gwt.core.client.JsArray;

public class Regions extends BaseServlet {
	public Regions() {
		super();
	}
	
	public Regions(RequestContext requestContext) {
		super(requestContext);
	}
	
	@Override
	public void response() {
		super.response();
		
		if (!this.isLoggedIn()) {
			super.redirectTo(new Login());
		} else {
			String method = this.getMethodTypeCtx();
			if(method == RequestContext.METHOD_POST) {
				Form form = (Form)this.requestContext.getArgs().get("form");
				RegionsData regionData = new RegionsData(new OnlineOfflineCallbacks(this) {
					public void onlineSuccessCallback(String results) {
						if(results != null) {
							RegionsData regiondata = new RegionsData();
							List regions = regiondata.getRegions(results);
							RequestContext requestContext = new RequestContext();
							requestContext.setMessageString("Region successfully saved");
							requestContext.getArgs().put("listing", regions);
							getServlet().redirectTo(new Regions(requestContext ));						
						} else {
							/*Error in saving the data*/			
						}
					}
					
					public void onlineErrorCallback(int errorCode) {
						Window.alert("GOT AN ERROR connecting to server");
						RequestContext requestContext = new RequestContext();
						if (errorCode == BaseData.ERROR_RESPONSE)
							requestContext.setMessageString("Unresponsive Server.  Please contact support.");
						else if (errorCode == BaseData.ERROR_SERVER)
							requestContext.setMessageString("Problem in the connection with the server.");
						else
							requestContext.setMessageString("Unknown error.  Please contact support.");
						getServlet().redirectTo(new Login(requestContext));	
					}
					
					public void offlineSuccessCallback(Object results) {
						if((Boolean)results) {
							RegionsData regiondata = new RegionsData();
							List regions = regiondata.getRegions();
							RequestContext requestContext = new RequestContext();
							requestContext.setMessageString("Region successfully saved");
							requestContext.getArgs().put("listing", regions);
							getServlet().redirectTo(new Regions(requestContext ));
						} else {
							RequestContext requestContext = new RequestContext();
							requestContext.setMessageString("Invalid data, please try again");
							getServlet().redirectTo(new Regions(requestContext));				
						}
						
					}
				}, form, this.requestContext.getQueryString());
				
				regionData.apply(regionData.postPageData());

			}
			else {
				this.fillTemplate(new RegionsTemplate(this.requestContext));
			}
			
		}
	}
}
