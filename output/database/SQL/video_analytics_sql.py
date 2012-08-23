from output.database.utility import *

# query constructor for malefeamle ratio pie chaart
def video_malefemale_ratio(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["P.GENDER as pie_key", "COUNT(*) as count"])
    sql_ds['from'].append('PERSON P')
    sql_ds['join'].append(["VIDEO_farmers_shown VFS", "P.id = VFS.person_id"])
    sql_ds['join'].append(["VIDEO VID","VID.id = VFS.video_id"])
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'P','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)

    sql_ds['group by'].append("P.GENDER")

    return join_sql_ds(sql_ds);



# query constructor for month wise production of videos bar graph.
def video_month_bar(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["COUNT( DISTINCT VID.ID ) AS count", "MONTH( VID.VIDEO_PRODUCTION_END_DATE ) AS MONTH","YEAR( VID.VIDEO_PRODUCTION_END_DATE ) AS YEAR"])
    sql_ds['from'].append("VIDEO VID");
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    sql_ds['group by'].extend(["YEAR","MONTH"])
    sql_ds['order by'].extend(["YEAR","MONTH"])
    return join_sql_ds(sql_ds)

def video_actor_wise_pie(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["actors as pie_key", "count(*) as count"])
    sql_ds['from'].append("VIDEO VID")
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    sql_ds['group by'].append("actors")

    return join_sql_ds(sql_ds)

def video_language_wise_scatter(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["L.language_name as name", "COUNT(VID.id) as count"])
    sql_ds['from'].append("LANGUAGE L");
    sql_ds['join'].append(["VIDEO VID", "VID.language_id = L.id"])
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    sql_ds['group by'].append("language_name")

    return join_sql_ds(sql_ds)

def video_tot_video(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("COUNT(DISTINCT VID.id ) AS count")
    sql_ds['from'].append("VIDEO VID");
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)

    return join_sql_ds(sql_ds)

# Query constructor for generating total distinct videos screened.
#arguments (geod, id) and (from_date, to_date) optional
def video_tot_scr(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("COUNT(DISTINCT SCR.video_id) AS count")
    sql_ds['from'].append("SCREENING_videoes_screened SCR");
    if(geog.upper()!="COUNTRY" or (to_date and from_date) or partners):
        sql_ds['join'].append(["SCREENING SC", "SC.id = SCR.screening_id"])
        filter_partner_geog_date(sql_ds,'SC','SC.DATE',geog,id,from_date,to_date,partners)

    return join_sql_ds(sql_ds)

# Query constructor for generating average time taken to produce video
#arguments (geod, id) and (from_date, to_date) optional
def video_avg_time(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("AVG(DATEDIFF(VIDEO_PRODUCTION_END_DATE ,VIDEO_PRODUCTION_START_DATE)+1) as avg")
    sql_ds['from'].append("VIDEO VID");
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)

    return join_sql_ds(sql_ds)

def video_type_wise_pie(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["VIDEO_TYPE as pie_key", "count(*) as count"])
    sql_ds['from'].append("VIDEO VID");
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    sql_ds['group by'].append('VIDEO_TYPE')

    return join_sql_ds(sql_ds)

def video_practice_wise_scatter(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    ##Change
    sql_ds['select'].extend(["PRACTICE_NAME as name","sec.name as sec","subsec.name as subsec","top.name as top","subtop.name as subtop","sub.name as sub", "COUNT(VID.id) as count"])
    #sql_ds['select'].extend(["PRACTICE_NAME as name","COUNT(VID.id) as count"])
    ##
    sql_ds['from'].append("VIDEO VID");
    sql_ds['join'].append(["PRACTICES P","VID.related_practice_id = P.id"])
    ##Change
    sql_ds['lojoin'].append(["practice_sector sec","sec.id = P.practice_sector_id"])
    sql_ds['lojoin'].append(["practice_subsector subsec","subsec.id = P.practice_subsector_id"])
    sql_ds['lojoin'].append(["practice_topic top","top.id = P.practice_topic_id"])
    sql_ds['lojoin'].append(["practice_subtopic subtop","subtop.id = P.practice_subtopic_id"])
    sql_ds['lojoin'].append(["practice_subject sub","sub.id = P.practice_subject_id"])
    ##
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    sql_ds['group by'].append("P.id")
    sql_ds['order by'].append("count")
    return join_sql_ds(sql_ds)

def video_min_date(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("MIN(VIDEO_PRODUCTION_END_DATE) as date")
    sql_ds['from'].append("VIDEO VID");
    sql_ds['where'].append('VID.VIDEO_SUITABLE_FOR = 1')
    filter_partner_geog_date(sql_ds,'VID','VID.VIDEO_PRODUCTION_END_DATE',geog,id,from_date,to_date,partners)
    return join_sql_ds(sql_ds)


#####################################
###  SQLs for VIDEO profile page ####
#####################################

#Logic: If a person adopts a practice,
# shown in the video, in 5-100 days of viewing;
# it counts as adoption for that video.
def get_adoption_for_video(id):
    return """SELECT COUNT(*) as tot_adopt 
        FROM PERSON_ADOPT_PRACTICE PAP
        JOIN (SELECT person_id, practices_id, DATE_ADD(DATE, INTERVAL 1 DAY) AS start, DATE_ADD(DATE, INTERVAL 100 DAY) AS end 
              FROM PERSON_MEETING_ATTENDANCE PMA
              JOIN SCREENING_videoes_screened SVS on SVS.screening_id = PMA.screening_id
              JOIN SCREENING SC on SC.id = PMA.screening_id
              JOIN VIDEO_related_agricultural_practices VRAP on VRAP.video_id = SVS.video_id
              WHERE SVS.video_id = """+str(id)+""") T 
    ON T.person_id = PAP.person_id AND T.practices_id = PAP.practice_id AND DATE_OF_ADOPTION BETWEEN start AND end
    """

#similar to above. ids is list of ids
def get_adoption_for_multiple_videos(ids):
    return """SELECT VID.id as id, count(PAP.id) as count
            FROM VIDEO VID
            LEFT OUTER JOIN SCREENING_videoes_screened  SVS ON SVS.video_id = VID.id
            LEFT OUTER JOIN PERSON_MEETING_ATTENDANCE PMA ON PMA.screening_id = SVS.screening_id
            LEFT OUTER JOIN SCREENING SC ON SC.id = SVS.screening_id
            LEFT OUTER JOIN VIDEO_related_agricultural_practices VRAP ON VRAP.video_id = SVS.video_id
            LEFT OUTER JOIN PERSON_ADOPT_PRACTICE PAP ON PAP.person_id = PMA.person_id
                AND (date_of_adoption BETWEEN DATE_ADD(DATE, INTERVAL 1 DAY)  AND DATE_ADD(DATE, INTERVAL 100 DAY))
                AND PAP.practice_id = VRAP.practices_id
            WHERE VID.id IN ("""+','.join(map(str,ids))+""")    
            GROUP BY VID.id"""

def get_screening_month_bar_for_video(id):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["COUNT( DISTINCT SC.ID ) AS count", "MONTH( SC.DATE ) AS MONTH","YEAR( SC.DATE ) AS YEAR"])
    sql_ds['from'].append("SCREENING_videoes_screened SVS");
    sql_ds['join'].append(["SCREENING SC", "SC.id = SVS.screening_id"])
    sql_ds['where'].append("SVS.video_id = "+str(id))
    sql_ds['group by'].extend(["YEAR","MONTH"])
    sql_ds['order by'].extend(["YEAR","MONTH"])
    return join_sql_ds(sql_ds)


