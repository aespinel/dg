package com.digitalgreen.dashboardgwt.client.data;

import com.digitalgreen.dashboardgwt.client.common.RequestContext;

public class PersonGroupsData extends BaseData {

	protected static String tableID = "12";
	protected static String createTable = "CREATE TABLE IF NOT EXISTS `person_groups` " +
												"(id INTEGER PRIMARY KEY  NOT NULL ," +
												"GROUP_NAME VARCHAR(100)  NOT NULL ," +
												"DAYS VARCHAR(9) NOT NULL ," +
												"TIMINGS TIME  NULL DEFAULT NULL," +
												"TIME_UPDATED DATETIME  NOT NULL ," +
												"village_id INT  NOT NULL DEFAULT 0, " +
												"FOREIGN KEY(village_id) REFERENCES village(id));"; 
	
	protected static String savePersonGroupOfflineURL = "/dashboard/savepersongroupoffline/";
	
	public PersonGroupsData() {
		super();
	}
	
	@Override
	protected String getTableId() {
		return PersonGroupsData.tableID;
	}
}