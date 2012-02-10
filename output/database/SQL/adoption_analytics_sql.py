from output.database.utility import *


def adoption_tot_ado(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("COUNT(DISTINCT PAP.id) AS tot_ado")
    sql_ds['select'].append("COUNT(DISTINCT person_id) as tot_farmers")
    sql_ds['select'].append("COUNT(DISTINCT practice_id) as tot_prac")
    sql_ds['from'].append("PERSON_ADOPT_PRACTICE PAP")
    if(geog != "COUNTRY" or partners):
        sql_ds['lojoin'].append(["PERSON P", "P.id = PAP.person_id"]);
        filter_partner_geog_date(sql_ds,'P','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
    else:
        filter_partner_geog_date(sql_ds,'PAP','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
        
    return join_sql_ds(sql_ds)

def adoption_exp_interest_to_adoption(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("COUNT(matched_adoption_id) AS tot_exp_int_ado, COUNT(*) AS tot_exp_int")
    sql_ds['from'].append('PERSON_MEETING_ATTENDANCE PMA')
    sql_ds['where'].append("interested = 1")
    if(from_date or to_date):
        sql_ds['lojoin'].append(["SCREENING SC", "SC.id = PMA.screening_id"]);
    if(geog != "COUNTRY" or partners):
       sql_ds['lojoin'].append(["PERSON P", "P.id = PMA.person_id"]);

    filter_partner_geog_date(sql_ds,'P','SC.DATE',geog,id,from_date,to_date,partners)
        
    return join_sql_ds(sql_ds)

def adoption_month_bar(geog,id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["COUNT(*) AS count","MONTH(DATE_OF_ADOPTION) AS MONTH", "YEAR(DATE_OF_ADOPTION) AS YEAR"])
    sql_ds['from'].append("PERSON_ADOPT_PRACTICE PAP")
    sql_ds['join'].append(["PERSON P", "P.id = PAP.person_id"])
    filter_partner_geog_date(sql_ds,"P","PAP.DATE_OF_ADOPTION",geog,id,from_date,to_date,partners);
    sql_ds['group by'].extend([ "YEAR", "MONTH"])
    return join_sql_ds(sql_ds);

def adoption_malefemale_ratio(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["P.GENDER as pie_key", "COUNT(*) as count"])
    sql_ds['from'].append('PERSON P')
    sql_ds['join'].append(["PERSON_ADOPT_PRACTICE PAP", "P.id = PAP.person_id"])
    filter_partner_geog_date(sql_ds,'P','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)

    sql_ds['group by'].append("P.GENDER")

    return join_sql_ds(sql_ds);

def adoption_practice_wise_scatter(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(["PRACTICE_NAME as name", "COUNT(PAP.id) as count"])
    sql_ds['from'].append("PERSON_ADOPT_PRACTICE PAP");
    sql_ds['join'].append(["PRACTICES PR","PAP.practice_id = PR.id"])
    sql_ds['join'].append(["PERSON P", "P.id = PAP.person_id"])
    filter_partner_geog_date(sql_ds,'P','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
    sql_ds['group by'].append("PRACTICE_NAME")
    sql_ds['order by'].append("count")
    return join_sql_ds(sql_ds)

def adoption_min_date(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("MIN(DATE_OF_ADOPTION) as date")
    sql_ds['from'].append("PERSON_ADOPT_PRACTICE PAP");
    if(geog != "COUNTRY" or partners):
        sql_ds['lojoin'].append(["PERSON P", "P.id = PAP.person_id"]);
        filter_partner_geog_date(sql_ds,'P','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
    else:
        filter_partner_geog_date(sql_ds,'PAP','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
    return join_sql_ds(sql_ds)

def adoption_repeat_adoption_practice_count(geog, id, from_date, to_date, partners):
    inner_sql_ds = get_init_sql_ds();
    inner_sql_ds['select'].append("DISTINCT person_id")
    inner_sql_ds['from'].append("PERSON_ADOPT_PRACTICE PAP")
    if(geog != "COUNTRY" or partners):
        inner_sql_ds['lojoin'].append(["PERSON P", "P.id = PAP.person_id"]);
        filter_partner_geog_date(inner_sql_ds,'P','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
    else:
        filter_partner_geog_date(inner_sql_ds,'PAP','PAP.DATE_OF_ADOPTION',geog,id,from_date,to_date,partners)
        
    inner_sql_ds['group by'].append("PAP.person_id")
    inner_sql_ds['group by'].append("PAP.practice_id")
    inner_sql_ds['having'].append("COUNT(*) > 1")
    
    sql_ds = get_init_sql_ds();
    sql_ds['select'].append("COUNT(*) as count")
    sql_ds['from'].append('(' + join_sql_ds(inner_sql_ds) + ') TAB')
    
    return join_sql_ds(sql_ds)

def adoption_rate_line(geog, id, from_date, to_date, partners):
    sql_ds = get_init_sql_ds();
    sql_ds['select'].extend(['date', 'SUM(total_adopted_attendees)', 'SUM(total_active_attendees)'])
    sql_ds['from'].append("village_precalculation VP")
    sql_ds['group by'].append('date')
    sql_ds['order by'].append('date')
    filter_partner_geog_date(sql_ds,'VP','VP.date',geog,id,from_date,to_date,partners)
    
    return join_sql_ds(sql_ds)
    