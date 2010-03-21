package com.digitalgreen.dashboardgwt.client.templates;

import java.util.HashMap;

import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.digitalgreen.dashboardgwt.client.servlets.Persons;

public class PersonsTemplate extends BaseTemplate{
	
	public PersonsTemplate(RequestContext requestContext) {
		super(requestContext);
	}
	
	@Override
	public void fill() {
		String templateType = "Person";
		String templatePlainType = "dashboard/person/add/";
		RequestContext requestContext = new RequestContext();
		HashMap args = new HashMap();
		args.put("action", "add");
		requestContext.setArgs(args);
		// Draw the content of the template depending on the request type (GET/POST)
		super.fillDGTemplate(templateType, personsListHtml, personsAddHtml, addDataToElementID);
		// Add it to the rootpanel
		super.fill();
		Persons addPersonsServlet = new Persons(requestContext);
		Persons savePerson = new Persons(new RequestContext(RequestContext.METHOD_POST));
		// Now add hyperlinks
		super.fillDGLinkControls(templatePlainType, templateType, personsListFormHtml, addPersonsServlet);
		// Now add any submit control buttons
		super.fillDGSubmitControls(savePerson);
	}

	final private String addDataToElementID[] = null;
	
	final static private String personsListFormHtml = "<div class='actions'>" +
								"<label>Action: <select name='action'>" +
									"<option value='' selected='selected'>---------</option>" +
									"<option value='delete_selected'>Delete selected persons</option>" +
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
												"Person name" +
											"</a>" +
										"</th>" +
										"<th>" +
										"<a href='?ot=asc&amp;o=2'>" +
											"Group" +
										"</a>" +
									"</th>" +
									"<th>" +
										"<a href='?ot=asc&amp;o=3'>" +
											"Village" +
										"</a>" +
									"</th>" +
								"</tr>" +
							"</thead>" +
							"<tbody>" +
								"<div id='data-rows'" +       // Insert data rows here
								"</div>" +
							"</tbody>" +
						"</table>";
	
	final static private String personsListHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
								"<div id='content' class='flex'>" +
									"<h1>Select Person to change</h1>" +
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
	
	final static private String personsAddHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" + 
								"<div id='content' class='colM'>" +
									"<h1>Add person</h1>" +
									"<div id='content-main'>" +
										"<form enctype='multipart/form-data' action='' method='post' id='person_form'>" +
											"<div>" +
												"<fieldset class='module aligned '>" +
													"<div class='form-row person_name  '>" +
														"<div>" +
															"<label for='id_person_name' class='required'>Person name:</label><input id='id_person_name' type='text' class='vTextField' name='person_name' maxlength='100' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row father_name  '>" +
														"<div>" +
															"<label for='id_father_name'>Father name:</label><input id='id_father_name' type='text' class='vTextField' name='father_name' maxlength='100' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row age  '>" +
														"<div>" +
															"<label for='id_age'>Age:</label><input id='id_age' type='text' class='vIntegerField' name='age' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row gender  '>" +
														"<div>" +
															"<label for='id_gender' class='required'>Gender:</label><select name='gender' id='id_gender'>" +
																"<option value='' selected='selected'>---------</option>" +
																"<option value='M'>Male</option>" +
																"<option value='F'>Female</option>" +
															"</select>" +
														"</div>" +
													"</div>" +
													"<div class='form-row phone_no  '>" +
														"<div>" +
															"<label for='id_phone_no'>Phone no:</label><input id='id_phone_no' type='text' class='vTextField' name='phone_no' maxlength='100' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row address  '>" +
														"<div>" +
															"<label for='id_address'>Address:</label><input id='id_address' type='text' class='vTextField' name='address' maxlength='500' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row land_holdings  '>" +
														"<div>" +
															"<label for='id_land_holdings'>Land holdings:</label><input id='id_land_holdings' type='text' class='vIntegerField' name='land_holdings' />" +
														"</div>" +
													"</div>" +
													"<div class='form-row village  '>" +
														"<div>" +
															"<label for='id_village' class='required'>Village:</label><input type='hidden' name='village' id='id_village' />" +
															"<style type='text/css' media='screen'>" +
												                "#lookup_village {" +
												                    "padding-right:16px;" +
												                    "background: url(" +
												                        "/media/img/admin/selector-search.gif" +
												                    ") no-repeat right;" +
												                "}" +
												                "#del_village {" +
												                    "display: none;" +
												                "}" +
											                "</style>" +
											                "<input type='text' id='lookup_village' value='' />" +
											                "<a href='#' id='del_village'>" +
											                	"<img src='/media/img/admin/icon_deletelink.gif' />" +
											                "</a>" +
											                "<script type='text/javascript'>" +
													            "if ($('#lookup_village').val()) {" +
													                "$('#del_village').show()" +
													            "}" +
													            "$('#lookup_village').autocomplete('../search/', {" +
													                "extraParams: {" +
													                    "search_fields: 'village_name'," +
													                    "app_label: 'dashboard'," +
													                    "model_name: 'village'," +
													                "}," +
													            "}).result(function(event, data, formatted) {" +
													                "if (data) {" +
													                    "$('#id_village').val(data[1]);" +
													                    "$('#del_village').show();" +
															    "filter();" +
													                "}" +
													            "});" +
													            "$('#del_village').click(function(ele, event) {" +
													                "$('#id_village').val('');" +
													                "$('#del_village').hide();" +
													                "$('#lookup_village').val('');" +
													            "});" +
													        "</script>" +
													    "</div>" +
													"</div>" +
													"<div class='form-row group  '>" +
														"<div>" +
															"<label for='id_group'>Group:</label><select name='group' id='id_group'>" +
																"<option value='' selected='selected'>---------</option>" +
															"</select>" +
														"</div>" +
													"</div>" +
												"</fieldset>" +
												"<div class='inline-group'>" +
												"<h2>Person Adopt Practices</h2>" +
												"<input type='hidden' name='personadoptpractice_set-TOTAL_FORMS' value='3' id='id_personadoptpractice_set-TOTAL_FORMS' /><input type='hidden' name='personadoptpractice_set-INITIAL_FORMS' value='0' id='id_personadoptpractice_set-INITIAL_FORMS' />" +
												"<div class='inline-related'>" +
													"<h3><b>Person Adopt Practice:</b>&nbsp; #1" +
													"</h3>" +
													"<fieldset class='module aligned '>" +
														"<div class='form-row practice  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-practice' class='required'>Practice:</label><select name='personadoptpractice_set-0-practice' id='id_personadoptpractice_set-0-practice'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row prior_adoption_flag  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-prior_adoption_flag'>Prior adoption flag:</label><select name='personadoptpractice_set-0-prior_adoption_flag' id='id_personadoptpractice_set-0-prior_adoption_flag'>" +
																	"<option value='1' selected='selected'>Unknown</option>" +
																	"<option value='2'>Yes</option>" +
																	"<option value='3'>No</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row date_of_adoption  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-date_of_adoption'>Date of adoption:</label><input id='id_personadoptpractice_set-0-date_of_adoption' type='text' class='vDateField' name='personadoptpractice_set-0-date_of_adoption' size='10' />" +
																"<span>&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);'>Today</a>&nbsp;|&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.openCalendar(0);' id='calendarlink0'>" +
																	"<img src='/media/img/admin/icon_calendar.gif' alt='Calendar'></a>" +
																"</span>" +
															"</div>" +
														"</div>" +
														"<div class='form-row quality  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-quality'>Quality:</label><input id='id_personadoptpractice_set-0-quality' type='text' class='vTextField' name='personadoptpractice_set-0-quality' maxlength='200' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-quantity'>Quantity:</label><input id='id_personadoptpractice_set-0-quantity' type='text' class='vIntegerField' name='personadoptpractice_set-0-quantity' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity_unit  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-0-quantity_unit'>Quantity unit:</label><input id='id_personadoptpractice_set-0-quantity_unit' type='text' class='vTextField' name='personadoptpractice_set-0-quantity_unit' maxlength='150' />" +
															"</div>" +
														"</div>" +
													"</fieldset>" +
													"<input type='hidden' name='personadoptpractice_set-0-id' id='id_personadoptpractice_set-0-id' />" +
													"<input type='hidden' name='personadoptpractice_set-0-person' id='id_personadoptpractice_set-0-person' />" +
												"</div>" +
												"<div class='inline-related'>" +
													"<h3><b>Person Adopt Practice:</b>&nbsp; #2" +
													"</h3>" +
													"<fieldset class='module aligned '>" +
														"<div class='form-row practice  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-practice' class='required'>Practice:</label><select name='personadoptpractice_set-1-practice' id='id_personadoptpractice_set-1-practice'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row prior_adoption_flag  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-prior_adoption_flag'>Prior adoption flag:</label><select name='personadoptpractice_set-1-prior_adoption_flag' id='id_personadoptpractice_set-1-prior_adoption_flag'>" +
																	"<option value='1' selected='selected'>Unknown</option>" +
																	"<option value='2'>Yes</option>" +
																	"<option value='3'>No</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row date_of_adoption  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-date_of_adoption'>Date of adoption:</label><input id='id_personadoptpractice_set-1-date_of_adoption' type='text' class='vDateField' name='personadoptpractice_set-1-date_of_adoption' size='10' />" +
																"<span>&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);'>Today</a>&nbsp;|&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.openCalendar(0);' id='calendarlink0'>" +
																	"<img src='/media/img/admin/icon_calendar.gif' alt='Calendar'></a>" +
																"</span>" +
															"</div>" +
														"</div>" +
														"<div class='form-row quality  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-quality'>Quality:</label><input id='id_personadoptpractice_set-1-quality' type='text' class='vTextField' name='personadoptpractice_set-1-quality' maxlength='200' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-quantity'>Quantity:</label><input id='id_personadoptpractice_set-1-quantity' type='text' class='vIntegerField' name='personadoptpractice_set-1-quantity' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity_unit  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-1-quantity_unit'>Quantity unit:</label><input id='id_personadoptpractice_set-1-quantity_unit' type='text' class='vTextField' name='personadoptpractice_set-1-quantity_unit' maxlength='150' />" +
															"</div>" +
														"</div>" +
													"</fieldset>" +
													"<input type='hidden' name='personadoptpractice_set-1-id' id='id_personadoptpractice_set-1-id' />" +
													"<input type='hidden' name='personadoptpractice_set-1-person' id='id_personadoptpractice_set-1-person' />" +
												"</div>" +
												"<div class='inline-related last-related'>" +
													"<h3><b>Person Adopt Practice:</b>&nbsp; #3" +
													"</h3>" +
													"<fieldset class='module aligned '>" +
														"<div class='form-row practice  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-practice' class='required'>Practice:</label><select name='personadoptpractice_set-2-practice' id='id_personadoptpractice_set-2-practice'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row prior_adoption_flag  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-prior_adoption_flag'>Prior adoption flag:</label><select name='personadoptpractice_set-2-prior_adoption_flag' id='id_personadoptpractice_set-2-prior_adoption_flag'>" +
																	"<option value='1' selected='selected'>Unknown</option>" +
																	"<option value='2'>Yes</option>" +
																	"<option value='3'>No</option>" +
																"</select>" +
															"</div>" +
														"</div>" +
														"<div class='form-row date_of_adoption  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-date_of_adoption'>Date of adoption:</label><input id='id_personadoptpractice_set-2-date_of_adoption' type='text' class='vDateField' name='personadoptpractice_set-2-date_of_adoption' size='10' />" +
																"<span>&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.handleCalendarQuickLink(0, 0);'>Today</a>&nbsp;|&nbsp;" +
																	"<a href='javascript:DateTimeShortcuts.openCalendar(0);' id='calendarlink0'>" +
																	"<img src='/media/img/admin/icon_calendar.gif' alt='Calendar'></a>" +
																"</span>" +
															"</div>" +
														"</div>" +
														"<div class='form-row quality  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-quality'>Quality:</label><input id='id_personadoptpractice_set-2-quality' type='text' class='vTextField' name='personadoptpractice_set-2-quality' maxlength='200' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-quantity'>Quantity:</label><input id='id_personadoptpractice_set-2-quantity' type='text' class='vIntegerField' name='personadoptpractice_set-2-quantity' />" +
															"</div>" +
														"</div>" +
														"<div class='form-row quantity_unit  '>" +
															"<div>" +
																"<label for='id_personadoptpractice_set-2-quantity_unit'>Quantity unit:</label><input id='id_personadoptpractice_set-2-quantity_unit' type='text' class='vTextField' name='personadoptpractice_set-2-quantity_unit' maxlength='150' />" +
															"</div>" +
														"</div>" +
													"</fieldset>" +
													"<input type='hidden' name='personadoptpractice_set-2-id' id='id_personadoptpractice_set-2-id' />" +
													"<input type='hidden' name='personadoptpractice_set-2-person' id='id_personadoptpractice_set-2-person' />" +
													"</div>" +
												"</div>" +
												"<div class='submit-row' >" +
													"<input type='submit' value='Save' class='default' name='_save' />" +
												"</div>" +
												"<script type='text/javascript'>document.getElementById('id_person_name').focus();</script>" +
												"<script type='text/javascript'>" +
												"</script>" +
											"</div>" +
										"</form>" +
									"</div>" +
									"<br class='clear' />" +
								"</div>";

}
