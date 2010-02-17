package com.digitalgreen.dashboardgwt.client.templates;

public class AnimatorsTemplate {

	final static private String animatorsListFormHtml = "<div class='actions'>" +
								"<label>Action: <select name='action'>" +
									"<option value='' selected='selected'>---------</option>" +
									"<option value='delete_selected'>Delete selected animators</option>" +
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
											"Name" +
											"</a>" +
										"</th>" +
										"<th>" +
											"<a href='?ot=asc&amp;o=2'>" +
											"Partner" +
											"</a>" +
										"</th>" +
										"<th>" +
											"<a href='?ot=asc&amp;o=3'>" +
											"Home village" +
											"</a>" +
										"</th>" +
									"</tr>" +
								"</thead>" +
								"<tbody>" +
									"<div id='data-rows'" +       // Insert data rows here
									"</div>" +
								"</tbody>" +
							"</table>";	

	final static private String animatorsListHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
								"<div id='content' class='flex'>" +
									"<h1>Select Animators to change</h1>" +
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
	
	final static private String animatorsAddHtml = "<link rel='stylesheet' type='text/css' href='/media/css/forms.css' />" +
							"<div id='content' class='colM'>" +
								"<h1>Add Animator</h1>" +
								"<div id='content-main'>" +
									"<form enctype='multipart/form-data' action='' method='post' id='animator_form'>" +
										"<div>" +
											"<fieldset class='module aligned '>" +
												"<div class='form-row name  '>" +
													"<div>" +
														"<label for='id_name' class='required'>Name:</label><input id='id_name' type='text' class='vTextField' name='name' maxlength='100' />" +
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
												"<div class='form-row csp_flag  '>" +
													"<div>" +
														"<label for='id_csp_flag'>Csp flag:</label><select name='csp_flag' id='id_csp_flag'>" +
															"<option value='1' selected='selected'>Unknown</option>" +
															"<option value='2'>Yes</option>" +
															"<option value='3'>No</option>" +
														"</select>" +
													"</div>" +
												"</div>" +
												"<div class='form-row camera_operator_flag  '>" +
													"<div>" +
														"<label for='id_camera_operator_flag'>Camera operator flag:</label><select name='camera_operator_flag' id='id_camera_operator_flag'>" +
															"<option value='1' selected='selected'>Unknown</option>" +
															"<option value='2'>Yes</option>" +
															"<option value='3'>No</option>" +
														"</select>" +
													"</div>" +
												"</div>" +
												"<div class='form-row facilitator_flag  '>" +
													"<div>" +
														"<label for='id_facilitator_flag'>Facilitator flag:</label><select name='facilitator_flag' id='id_facilitator_flag'>" +
															"<option value='1' selected='selected'>Unknown</option>" +
															"<option value='2'>Yes</option>" +
															"<option value='3'>No</option>" +
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
												"<div class='form-row partner  '>" +
													"<div>" +
														"<label for='id_partner' class='required'>Partner:</label><select name='partner' id='id_partner'>" +
															"<option value='' selected='selected'>---------</option>" +
														"</select><a href='/admin/dashboard/partners/add/' class='add-another' id='add_id_partner' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
													"</div>" +
												"</div>" +
												"<div class='form-row home_village  '>" +
													"<div>" +
														"<label for='id_home_village' class='required'>Home village:</label><select name='home_village' id='id_home_village'>" +
															"<option value='' selected='selected'>---------</option>" +
														"</select><a href='/admin/dashboard/village/add/' class='add-another' id='add_id_home_village' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
													"</div>" +
												"</div>" +
											"</fieldset>" +
											"<div class='inline-group'>" +
												"<h2>Animator Assigned Villages</h2>" +
												"<input type='hidden' name='animatorassignedvillage_set-TOTAL_FORMS' value='3' id='id_animatorassignedvillage_set-TOTAL_FORMS' /><input type='hidden' name='animatorassignedvillage_set-INITIAL_FORMS' value='0' id='id_animatorassignedvillage_set-INITIAL_FORMS' />" +
												"<div class='inline-related'>" +
													"<h3><b>Animator Assigned Village:</b>&nbsp; #1" +
													"</h3>" +
													"<fieldset class='module aligned '>" +  
														"<div class='form-row village  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-0-village' class='required'>Village:</label><select name='animatorassignedvillage_set-0-village' id='id_animatorassignedvillage_set-0-village'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select><a href='/admin/dashboard/village/add/' class='add-another' id='add_id_animatorassignedvillage_set-0-village' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
															"</div>" +
														"</div>" +
														"<div class='form-row start_date  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-0-start_date'>Start date:</label><input id='id_animatorassignedvillage_set-0-start_date' type='text' class='vDateField' name='animatorassignedvillage_set-0-start_date' size='10' />" +
															"</div>" +
														"</div>" +
													"</fieldset>" +
													"<input type='hidden' name='animatorassignedvillage_set-0-id' id='id_animatorassignedvillage_set-0-id' />" +
													"<input type='hidden' name='animatorassignedvillage_set-0-animator' id='id_animatorassignedvillage_set-0-animator' />" +
												"</div>" +
												"<div class='inline-related'>" +
													"<h3><b>Animator Assigned Village:</b>&nbsp; #2" +
													"</h3>" +
													"<fieldset class='module aligned '>" +
														"<div class='form-row village  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-1-village' class='required'>Village:</label><select name='animatorassignedvillage_set-1-village' id='id_animatorassignedvillage_set-1-village'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select><a href='/admin/dashboard/village/add/' class='add-another' id='add_id_animatorassignedvillage_set-1-village' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
															"</div>" +
														"</div>" +
														"<div class='form-row start_date  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-1-start_date'>Start date:</label><input id='id_animatorassignedvillage_set-1-start_date' type='text' class='vDateField' name='animatorassignedvillage_set-1-start_date' size='10' />" +
															"</div>" +      
														"</div>" +
													"</fieldset>" +  
													"<input type='hidden' name='animatorassignedvillage_set-1-id' id='id_animatorassignedvillage_set-1-id' />" +
													"<input type='hidden' name='animatorassignedvillage_set-1-animator' id='id_animatorassignedvillage_set-1-animator' />" +
												"</div>" +
												"<div class='inline-related last-related'>" +
													"<h3><b>Animator Assigned Village:</b>&nbsp; #3" +
													"</h3>" +
													"<fieldset class='module aligned '>" +
														"<div class='form-row village  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-2-village' class='required'>Village:</label><select name='animatorassignedvillage_set-2-village' id='id_animatorassignedvillage_set-2-village'>" +
																	"<option value='' selected='selected'>---------</option>" +
																"</select><a href='/admin/dashboard/village/add/' class='add-another' id='add_id_animatorassignedvillage_set-2-village' onclick='return showAddAnotherPopup(this);'> <img src='/media/img/admin/icon_addlink.gif' width='10' height='10' alt='Add Another'/></a>" +
															"</div>" +
														"</div>" +
														"<div class='form-row start_date  '>" +
															"<div>" +
																"<label for='id_animatorassignedvillage_set-2-start_date'>Start date:</label><input id='id_animatorassignedvillage_set-2-start_date' type='text' class='vDateField' name='animatorassignedvillage_set-2-start_date' size='10' />" +
															"</div>" +
														"</div>" +
													"</fieldset>" +
													"<input type='hidden' name='animatorassignedvillage_set-2-id' id='id_animatorassignedvillage_set-2-id' />" +
													"<input type='hidden' name='animatorassignedvillage_set-2-animator' id='id_animatorassignedvillage_set-2-animator' />" +
												"</div>" +
											"</div>" +
											"<div class='submit-row' >" +
												"<input type='submit' value='Save' class='default' name='_save' />" +
												"<input type='submit' value='Save and add another' name='_addanother'  />" +
												"<input type='submit' value='Save and continue editing' name='_continue' />" +
											"</div>" +
											"<script type='text/javascript'>document.getElementById('id_name').focus();</script>" +
											"<script type='text/javascript'>" +
											"</script>" +
										"</div>" +
									"</form>" +
								"</div>" +
							"</div>";
}
