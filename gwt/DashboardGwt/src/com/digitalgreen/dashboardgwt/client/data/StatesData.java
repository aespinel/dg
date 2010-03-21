package com.digitalgreen.dashboardgwt.client.data;

import java.util.ArrayList;
import java.util.List;

import com.digitalgreen.dashboardgwt.client.common.Form;
import com.digitalgreen.dashboardgwt.client.common.OnlineOfflineCallbacks;
import com.digitalgreen.dashboardgwt.client.common.RequestContext;
import com.google.gwt.core.client.JsArray;
import com.google.gwt.gears.client.database.DatabaseException;
import com.google.gwt.user.client.Window;

public class StatesData extends BaseData {
	
	public static class Type extends BaseData.Type{
		protected Type() {}
		public final native String getStateName() /*-{ return this.fields.state_name; }-*/;
		public final native RegionsData.Type getRegion() /*-{ return this.fields.region }-*/;
		public final native String getStartDate() /*-{ return this.fields.start_date; }-*/;
	}
	
	public class Data extends BaseData.Data {
		
		final private static String COLLECTION_PREFIX = "state";
			
		private String state_name;
		private String start_date;
		//private int region_id;
		private RegionsData.Data region;
		
		
		public Data() {
			super();
		}

		public Data(int id, String state_name,String start_date, RegionsData.Data region) {
			super();
			this.id = id;
			this.state_name = state_name;
			this.start_date = start_date;
			this.region = region;
		}
		
		/*public Data(int id, String state_name, int region_id, String start_date) {
			super();
			this.id = id;
			this.state_name = state_name;
			this.region_id = region_id;
			this.start_date = start_date;
		}*/
		
		public String getStateName(){
			return this.state_name;
		}
		
		public String getStartDate(){
			return this.start_date;
		}

		
		/*public int getRegionId(){
			return this.region_id;
		}*/
		
		public RegionsData.Data getRegion(){
			return this.region;
		}
		
		public Object clone() {
			Data obj = new Data();
			obj.id = this.id;
			obj.state_name = this.state_name;
			obj.region = this.region;
			obj.start_date = this.start_date;
			return obj;
		}
		
		@Override
		public String getPrefixName() {
			return Data.COLLECTION_PREFIX;
		}
		
		@Override
		public void setObjValueFromString(String key, Object val) {		
			if(key.equals("id")) {
				this.id = ((Integer)val).intValue();
			} else if(key.equals("state_name")) {
				this.state_name = (String)val;
			} else if(key.equals("region")) {
				// Have to Create an instance of RegionsData to create an instance of RegionsData.Data -- any better way of doing this??
				RegionsData region1 = new RegionsData();
				this.region = region1.getNewData();
				this.region.id = Integer.parseInt((String)val);
				//Never ever use this -- this.region.id = ((Integer)val).intValue();
			}  else if(key.equals("start_date")) {
				this.start_date = (String)val;
			}		
		}
		
		@Override
		public void save() {
			StatesData statesDataDbApis = new StatesData();			
			this.id = statesDataDbApis.autoInsert(this.state_name, Integer.valueOf(this.region.getId()).toString(), this.start_date);
		}
	}

	protected static String tableID = "05";
	final protected static String createTable = "CREATE TABLE IF NOT EXISTS `state` " +
												"(id INTEGER PRIMARY KEY  NOT NULL ," +
												"STATE_NAME VARCHAR(100)  NOT NULL ," +
												"region_id INT  NOT NULL DEFAULT 0," +
												"START_DATE DATE  NULL DEFAULT NULL, " +
												"FOREIGN KEY(region_id) references region(id));"; 

	protected static String listStates = "SELECT * FROM state JOIN region ON state.region_id = region.id ORDER BY (-state.id);";
	protected static String saveStateURL = "/dashboard/savestate/";
	protected static String getStateURL = "/dashboard/getstates/";
	protected String table_name = "state";
	protected String[] fields = {"id", "state_name", "region_id", "start_date"};
	
	public StatesData() {
		super();
	}
	
	public StatesData(OnlineOfflineCallbacks callbacks) {
		super(callbacks);
	}
	
	public StatesData(OnlineOfflineCallbacks callbacks, Form form, String queryString) {
		super(callbacks, form, queryString);
	}

	@Override
	public Data getNewData() {
		return new Data();
	}
	
	@Override
	protected String getTableId() {
		return StatesData.tableID;
	}
	
	protected String getTableName() {
		return this.table_name;
	}
	
	protected String[] getFields() {
		return this.fields;
	}
	
	public final native JsArray<Type> asArrayOfData(String json) /*-{
		return eval(json);
	}-*/;
	
	public List serialize(JsArray<Type> stateObjects){
		List states = new ArrayList();
		RegionsData region = new RegionsData();
		for(int i = 0; i < stateObjects.length(); i++){
			RegionsData.Data r = region. new Data(Integer.parseInt(stateObjects.get(i).getRegion().getPk()), stateObjects.get(i).getRegion().getRegionName(), stateObjects.get(i).getRegion().getStartDate()) ;
			Data state = new Data(Integer.parseInt(stateObjects.get(i).getPk()), stateObjects.get(i).getStateName(), stateObjects.get(i).getStartDate(), r );
			states.add(state);
		}
		
		return states;
	}
	
	public List getStates(String json){
		return this.serialize(this.asArrayOfData(json));		
	}
	
	public List getStates(){
		BaseData.dbOpen();
		List states = new ArrayList();
		RegionsData region = new RegionsData();
		this.select(listStates);
		if (this.getResultSet().isValidRow()){
			try {
				for (int i = 0; this.getResultSet().isValidRow(); ++i, this.getResultSet().next()) {
					RegionsData.Data r = region. new Data(this.getResultSet().getFieldAsInt(4),  this.getResultSet().getFieldAsString(5), this.getResultSet().getFieldAsString(6)) ;
					Data state = new Data(this.getResultSet().getFieldAsInt(0), this.getResultSet().getFieldAsString(1), this.getResultSet().getFieldAsString(3), r);
					states.add(state);
	    	      }				
			} catch (DatabaseException e) {
				Window.alert("Database Exception : " + e.toString());
				// TODO Auto-generated catch block
				BaseData.dbClose();
			}
			
		}
		BaseData.dbClose();
		return states;
	}

	public List getTemplateDataOnline(String json){
		List relatedData = null;
		return relatedData;
	}
	
	public Object postPageData() {
		if(BaseData.isOnline()){
			this.post(RequestContext.SERVER_HOST + StatesData.saveStateURL, this.queryString);
		}
		else{
			this.save();
			return true;
		}
		
		return false;
	}
	
	public Object getListPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + StatesData.getStateURL);
		}
		else{
			return true;
		}
		return false;
	}	
	
	public String retrieveDataAndConvertResultIntoHtml(){
		RegionsData regionData = new RegionsData();
		List regions = regionData.getRegions();
		RegionsData.Data region;
		String html = "<select name=\"region\" id=\"id_region\">";
		for(int i=0; i< regions.size(); i++){
			region = (RegionsData.Data)regions.get(i);
			html = html + "<option value = \"" + region.getId() +"\">" + region.getRegionName() + "</option>";
		}
		html = html + "</select>";
		return html;
	}
	
	public Object getAddPageData(){
		if(BaseData.isOnline()){
			this.get(RequestContext.SERVER_HOST + StatesData.saveStateURL);
		}
		else{
			return retrieveDataAndConvertResultIntoHtml();
		}
		return false;
	}
}