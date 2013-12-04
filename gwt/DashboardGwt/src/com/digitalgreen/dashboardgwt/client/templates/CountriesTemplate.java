package com.digitalgreen.dashboardgwt.client.templates;

import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.data.CountriesData;
import com.digitalgreen.dashboardgwt.client.servlets.Countries;
import com.google.gwt.user.client.Window;
import com.google.gwt.user.client.ui.Hyperlink;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class CountriesTemplate extends BaseTemplate {
	public CountriesTemplate(RequestContext requestContext) {
		super(requestContext);
		this.formTemplate = new Form((new CountriesData()).getNewData());
	}
	
	@Override
	public void fill() {
		String templateType = "Country";
		String templatePlainType = "dashboard/country/add/";
		RequestContext requestContext = new RequestContext();
		HashMap args = new HashMap();
		args.put("action", "add");
		requestContext.setArgs(args);
		requestContext.setForm(this.formTemplate);
		Countries addCountryServlet = new Countries(requestContext);
		RequestContext saveRequestContext = new RequestContext(RequestContext.METHOD_POST);
		saveRequestContext.setForm(this.formTemplate);
		Countries saveCountry = new Countries(saveRequestContext);
		// Draw the content of the template depending on the request type (GET/POST)
		super.fillDGTemplate(templateType, countriesListHtml, countriesAddHtml, addDataToElementID);
		// Add it to the rootpanel
		super.fill();
		//Now add listings
		List<Hyperlink> links =  this.fillListings();
		// Now add hyperlinks
		super.fillDgListPage(templatePlainType, templateType, countriesListFormHtml, addCountryServlet, links);
		this.displayCalendar();
		// Now add any submit control buttons
		super.fillDgFormPage(saveCountry);
	}
	
	protected List<Hyperlink> fillListings() {
		HashMap queryArgs = this.getRequestContext().getArgs();
		String queryArg = (String)queryArgs.get("action");
		List<Hyperlink> links = new ArrayList<Hyperlink>();
		// If we're unsure, just default to list view
		if(queryArg.equals("list")) {
			// 	Add Listings
			List countries = (List)queryArgs.get("listing");			
			if(countries  != null){
				String tableRows ="";
				String style;
				CountriesData.Data country;
				RequestContext requestContext = null;
				for (int row = 0; row < countries.size(); ++row) {
					if(row%2==0)
						style= "row2";
					else
						style = "row1";
					country = (CountriesData.Data) countries.get(row);
					requestContext = new RequestContext();
					requestContext.getArgs().put("action", "edit");
					requestContext.getArgs().put("id", country.getId());
					requestContext.setForm(this.formTemplate);
					links.add(this.createHyperlink("<a href='#dashboard/country/" + country.getId() + "/'>" +
							country.getCountryName() + "</a>",
							"dashboard/country/" + country.getId() + "/",
							new Countries(requestContext)));
					tableRows += "<tr class='" + style + "'><td><input type='checkbox' class='action-select' value='" + 
								country.getId() + "' name='_selected_action' /></td>" +
								"<th id = 'row" + row + "'></th></tr>";
				}
				countriesListFormHtml = countriesListFormHtml + tableRows + "</tbody></table>";
			}
		}
		return links;
	}
	//Loading javascript for displaying calendar in Google chrome browser
	public static native void displayCalendar() /*-{
		$wnd.DateTimeShortcuts.init();		
	}-*/;
	
	final private String addDataToElementID[] = null;
	
	private String countriesListFormHtml = "<script type='text/javascript' src='/media/js/admin/DateTimeShortcuts.js'></script>" +
						"<script type='text/javascript' src='/media/js/calendar.js'></script>" +
						"<div class='actions'>" +
						"<label>Action: <select name='action'>" +
							"<option value='' selected='selected'>---------</option>" +
							"<option value='delete_selected'>Delete selected countries</option>" +
							"</select>" +
						"</label>" +
						"<button type='submit' class='button' title='Run the selected action' name='index' value='0'>Go</button>" +
					"</div>" +
					"<table cellspacing='0'>" +
						"<thead>" +
							"<tr>" +
								"<th>" +
									"<input type='checkbox' id='action-toggle' />" +
								"</th>" +
								"<th>" +
									"<a href='?ot=asc&amp;o=1'>" +
										"Country" +
									"</a>" +
								"</th>" +
							"</tr>" +
						"</thead>" +
						"<tbody>";

	final  private String countriesListHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
						"<div id='content' class='flex'>" +
							"<h1>Select country to change</h1>" +
							"<div id='content-main'>" +
								"<ul class='object-tools'>" +
									"<li id='add-link'>" +                // Insert add link here
									"</li>" +
								"</ul>" +
								"<div class='module' id='changelist'>" +
									"<form action='' method='post'>" +
										"<div id='listing-form-body'>" +  // Insert form data here
										"</div>" +
									"</form>" +
								"</div>" +
							"</div>" +
						"</div>";
	
	final  private String countriesAddHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
		"<div id='content' class='colM'>" +
			"<h1>Add Countries</h1>" +
			"<div id='content-main'>" +
				"<fieldset class='module aligned '>" +
					"<div class='form-row country_name  '>" +
						"<div>" +
							"<label for='id_country_name' class='required'>Country name:</label><input id='id_country_name' type='text' class='vTextField' name='country_name' maxlength='100' />" +
						"</div>" +
					"</div>" +
					"<div class='form-row start_date'>" +
						"<div>" +
							"<label for='id_start_date'>Start date:</label>" +	
							"<input id='id_start_date' type='text' class='vDateField' name='start_date' size='10' />" +
						"</div>" + 
					"</div>" +
				"</fieldset>" +
				"<div class='submit-row'>" +
					"<input id='save' type='button' value='Save' class='default' name='_save' />" +
				"</div>" +
			"</div>" +
		"</div>" ;
	}