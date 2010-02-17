package com.digitalgreen.dashboardgwt.client.templates;

public class DisctrictTemplate {
	
	final static private String districtListFormHtml = "<div class='actions'>" +
								"<label>Action: <select name='action'>" +
									"<option value='' selected='selected'>---------</option>" +
									"<option value='delete_selected'>Delete selected districts</option>" +
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
												"District name" +
											"</a>" +
										"</th>" +
										"<th>" +
											"<a href='?ot=asc&amp;o=2'>" +
												"State" +
											"</a>" +
										"</th>" +
										"<th>" +
											"<a href='?ot=asc&amp;o=3'>" +
												"Fieldofficer" +
											"</a>" +
										"</th>" +
										"<th>" +
											"<a href='?ot=asc&amp;o=4'>" +
												"Partner" +
											"</a>" +
										"</th>" +
									"</tr>" +
								"</thead>" +
								"<tbody>" +
									"<div id='data-rows'" +       // Insert data rows here
									"</div>" +
								"</tbody>" +
							"</table>";
	
	final static private String districtFormHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
								"<div id='content' class='flex'>" +
									"<h1>Select region to change</h1>" +
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
	
	final static private String districtAddHtml =  "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
						"<div id='content' class='colM'>" +
						"<h1>Add district</h1>" +
							"<div id='content-main'>" +
								"<form enctype='multipart/form-data' action='' method='post' id='district_form'>" +
									"<div>" +
										"<fieldset class='module aligned '>" +
											"<div class='form-row district_name  '>" +
												"<div>" +
													"<label for='id_district_name' class='required'>District name:</label><input id='id_district_name' type='text' class='vTextField' name='district_name' maxlength='100' />" +
												"</div>" +
											"</div>" +
											"<div class='form-row start_date  '>" +
												"<div>" +
													"<label for='id_start_date'>Start date:</label><input id='id_start_date' type='text' class='vDateField' name='start_date' size='10' />" +
												"</div>" +
											"</div>" +
											"<div class='form-row state  '>" +
												"<div>" +
													"<label for='id_state' class='required'>State:</label><select name='state' id='id_state'>" +
														"<option value='' selected='selected'>---------</option>" +
													"</select><a href='/admin/dashboard/state/add/' class='add-another' id='add_id_state' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
													"</div>" +
											"</div>" +
											"<div class='form-row fieldofficer  '>" +
												"<div>" +
													"<label for='id_fieldofficer' class='required'>Fieldofficer:</label><select name='fieldofficer' id='id_fieldofficer'>" +
														"<option value='' selected='selected'>---------</option>" +
													"</select><a href='/admin/dashboard/fieldofficer/add/' class='add-another' id='add_id_fieldofficer' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
												"</div>" +
											"</div>" +
											"<div class='form-row fieldofficer_startday  '>" +
												"<div>" +
													"<label for='id_fieldofficer_startday'>Fieldofficer startday:</label><input id='id_fieldofficer_startday' type='text' class='vDateField' name='fieldofficer_startday' size='10' />" +
												"</div>" +
											"</div>" +
											"<div class='form-row partner  '>" +
												"<div>" +
													"<label for='id_partner' class='required'>Partner:</label><select name='partner' id='id_partner'>" +
														"<option value='' selected='selected'>---------</option>" +
													"</select><a href='/admin/dashboard/partners/add/' class='add-another' id='add_id_partner' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
												"</div>" +
											"</div>" +
										"</fieldset>" +
										"<div class='submit-row' >" +
											"<input type='submit' value='Save' class='default' name='_save' />" +
											"<input type='submit' value='Save and add another' name='_addanother'  />" +
											"<input type='submit' value='Save and continue editing' name='_continue' />" +
										"</div>" +
										"<script type='text/javascript'>document.getElementById('id_district_name').focus();</script>" +
										"<script type='text/javascript'>" +
										"</script>" +
									"</div>" +
								"</form>" +
							"</div>" +
						"</div>";
}