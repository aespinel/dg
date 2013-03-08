from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from farmerbook import farmer_book_views
from static_site_views import home
from views import *
from output.views import overview_analytics, screening_analytics, video_analytics, adoption_analytics, targets
from output.views.common import drop_down_val, overview_line_graph, practice_change
from static_site_views import *
from path.views import page, update
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from dashboard.data_log import send_updated_log
admin.autodiscover()

urlpatterns = patterns('',
    (r'coco/offline/$', direct_to_template, {'template': 'dashboard.html'}), 
    (r'cocoproto/offline/$', direct_to_template, {'template': 'dashboard_offline.html'}), 
    (r'^coco/', redirect_url),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^api/', include('dashboard.urls')),
    (r'^tastypie/post/?$',tastypie_post),
    (r'^feeds/persons/$', feed_person_html_on_person_group),
    (r'^feeds/persons/modified/$', feed_person_html_on_person_group_modified),
    (r'^feeds/person_pract/$',feed_person_prac_pg_anim),
    (r'^feeds/person_pract/$',feed_person_prac_pg_anim),
    (r'^get/person/$',get_person),
    (r'^feeds/persons_village/(\d+)/$', feeds_persons_village),
    (r'^feeds/test/(\d+)/$', test),
    (r'^feeds/test_gwt/(\d+)/$', test_gwt),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^animators-by-village-id/(\d+)/$', feed_animators),
    (r'/search/', search),
    (r'^dashboard/getkey/$', get_key_for_user),
    (r'^dashboard/setkey/$', set_key_for_user),
    (r'^dashboard/login/$', login_view),
    (r'^dashboard/savecountryonline/((?P<id>\d*)/)?$', save_country_online),
    (r'^dashboard/getcountriesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_countries_online),
    (r'^dashboard/savecountryoffline/((?P<id>\d*)/)?$', save_country_offline),
    (r'^dashboard/saveregiononline/((?P<id>\d*)/)?$', save_region_online),
    (r'^dashboard/getregionsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_regions_online),
    (r'^dashboard/saveregionoffline/((?P<id>\d*)/)?$', save_region_offline),
    (r'^dashboard/savestateonline/((?P<id>\d*)/)?$', save_state_online),
    (r'^dashboard/getstatesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_states_online),
    (r'^dashboard/savestateoffline/((?P<id>\d*)/)?$', save_state_offline),
    (r'^dashboard/savefieldofficeronline/((?P<id>\d*)/)?$', save_fieldofficer_online),
    (r'^dashboard/getfieldofficersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_fieldofficers_online),
    (r'^dashboard/savefieldofficeroffline/((?P<id>\d*)/)?$', save_fieldofficer_offline),
    (r'^dashboard/savepracticeonline/((?P<id>\d*)/)?$', save_practice_online),
    (r'^dashboard/getpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_practices_online),
    (r'^dashboard/savepracticeoffline/((?P<id>\d*)/)?$', save_practice_offline),
    (r'^dashboard/getpracticesseenforperson/((?P<person_id>\d*)/)?$',get_practices_seen_for_person),
    (r'^dashboard/savelanguageonline/((?P<id>\d*)/)?$', save_language_online),
    (r'^dashboard/getlanguagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_languages_online),
    (r'^dashboard/savelanguageoffline/((?P<id>\d*)/)?$', save_language_offline),
    (r'^dashboard/savepartneronline/((?P<id>\d*)/)?$', save_partner_online),
    (r'^dashboard/getpartnersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_partners_online),
    (r'^dashboard/savepartneroffline/((?P<id>\d*)/)?$', save_partner_offline),
    (r'^dashboard/savevideoonline/((?P<id>\d*)/)?$', save_video_online),
    (r'^dashboard/getvideosonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_videos_online),
    (r'^dashboard/getvideosseenforperson/((?P<person_id>\d*)/)?$', get_videos_seen_for_person),
    (r'^dashboard/savevideooffline/((?P<id>\d*)/)?$', save_video_offline),
    (r'^dashboard/savevideofarmersonline/', save_personshowninvideo_online),
    (r'^dashboard/getvideofarmersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personshowninvideo_online),
    (r'^dashboard/savevideofarmersoffline/((?P<id>\d*)/)?$', save_personshowninvideo_offline),
    (r'^dashboard/savedevelopmentmanageronline/((?P<id>\d*)/)?$', save_developmentmanager_online),
    (r'^dashboard/getdevelopmentmanagersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_developmentmanagers_online),
    (r'^dashboard/savedevelopmentmanageroffline/((?P<id>\d*)/)?$', save_developmentmanager_offline),
    (r'^dashboard/saveequipmentonline/((?P<id>\d*)/)?$', save_equipment_online),
    (r'^dashboard/getequipmentsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_equipments_online),
    (r'^dashboard/saveequipmentoffline/((?P<id>\d*)/)?$', save_equipment_offline),
    (r'^dashboard/savedistrictonline/((?P<id>\d*)/)?$', save_district_online),
    (r'^dashboard/getdistrictsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_districts_online),
    (r'^dashboard/savedistrictoffline/((?P<id>\d*)/)?$', save_district_offline),
    (r'^dashboard/saveblockonline/((?P<id>\d*)/)?$', save_block_online),
    (r'^dashboard/getblocksonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_blocks_online),
    (r'^dashboard/getblocksfordistrictonline/((?P<district_id>\d*)/)?$', get_blocks_for_district_online),
    (r'^dashboard/saveblockoffline/((?P<id>\d*)/)?$', save_block_offline),
    (r'^dashboard/savevillageonline/((?P<id>\d*)/)?$', save_village_online ),
    (r'^dashboard/getvillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_villages_online),
    (r'^dashboard/getvillagesforblocksonline/((?P<block_id>\d*)/)?$', get_villages_for_blocks_online),
    (r'^dashboard/savevillageoffline/((?P<id>\d*)/)?$', save_village_offline),
    (r'^dashboard/saveanimatoronline/((?P<id>\d*)/)?$', save_animator_online),
    (r'^dashboard/getanimatorsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animators_online),
    (r'^dashboard/saveanimatoroffline/((?P<id>\d*)/)?$', save_animator_offline),
    (r'^dashboard/saveanimatorassignedvillageonline/((?P<id>\d*)/)?$', save_animatorassignedvillage_online),
    (r'^dashboard/getanimatorassignedvillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animatorassignedvillages_online),
    (r'^dashboard/saveanimatorassignedvillageoffline/((?P<id>\d*)/)?$', save_animatorassignedvillage_offline),
    (r'^dashboard/savepersongrouponline/((?P<id>\d*)/)?$', save_persongroup_online),
    (r'^dashboard/getpersongroupsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_persongroups_online),
    (r'^dashboard/getpersongroupsforvillageonline/((?P<village_id>\d*)/)?$', get_persongroups_for_village_online),
    (r'^dashboard/savepersongroupoffline/((?P<id>\d*)/)?$', save_persongroup_offline),
    (r'^dashboard/savepersononline/((?P<id>\d*)/)?$', save_person_online),
    (r'^dashboard/getpersonsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_persons_online),
    (r'^dashboard/getpersonforvillageandnopersongrouponline/((?P<village_id>\d*)/)?$', get_person_for_village_and_no_person_group_online),
    (r'^dashboard/getpersonforpersongrouponline/((?P<group_id>\d*)/)?$', get_person_for_person_group_online),
    (r'^dashboard/savepersonoffline/((?P<id>\d*)/)?$', save_person_offline),
    (r'^dashboard/savescreeningonline/((?P<id>\d*)/)?$', save_screening_online),
    (r'^dashboard/getscreeningsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_screenings_online),
    (r'^dashboard/savescreeningoffline/((?P<id>\d*)/)?$', save_screening_offline),
    (r'^dashboard/getattendance/((?P<id>\d*)/)?$', get_attendance),
    (r'^dashboard/getscreeningfarmergroupstargetedsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$',get_groupstargetedinscreening_online),
    (r'^dashboard/savescreeningfarmergroupstargetedsoffline/((?P<id>\d*)/)?$',save_groupstargetedinscreening_offline),
    (r'^dashboard/savescreeningvideosscreenedsonline/$', save_videosscreenedinscreening_online),
    (r'^dashboard/getscreeningvideosscreenedsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_videosscreenedinscreening_online),
    (r'^dashboard/savescreeningvideosscreenedsoffline/((?P<id>\d*)/)?$', save_videosscreenedinscreening_offline),
    (r'^dashboard/savetrainingonline/((?P<id>\d*)/)?$', save_training_online),
    (r'^dashboard/gettrainingsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_trainings_online),
    (r'^dashboard/savetrainingoffline/((?P<id>\d*)/)?$', save_training_offline),
    (r'^dashboard/savetraininganimatorstrainedonline/?$', save_traininganimatorstrained_online),
    (r'^dashboard/gettraininganimatorstrainedonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_traininganimatorstrained_online),
    (r'^dashboard/savetraininganimatorstrainedoffline/((?P<id>\d*)/)?$', save_traininganimatorstrained_offline),
    (r'^dashboard/savemonthlycostpervillageonline/$', save_monthlycostpervillage_online),
    (r'^dashboard/getmonthlycostpervillagesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_monthlycostpervillages_online),
    (r'^dashboard/savemonthlycostpervillageoffline/((?P<id>\d*)/)?$', save_monthlycostpervillage_offline),
    (r'^dashboard/saveanimatorsalarypermonthonline/$', save_animatorsalarypermonth_online),
    (r'^dashboard/getanimatorsalarypermonthsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_animatorsalarypermonths_online),
    (r'^dashboard/saveanimatorsalarypermonthoffline/((?P<id>\d*)/)?$', save_animatorsalarypermonth_offline),
    (r'^dashboard/savepersonrelationonline/$', save_personrelation_online),
    (r'^dashboard/getpersonrelationsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personrelations_online),
    (r'^dashboard/savepersonrelationoffline/((?P<id>\d*)/)?$', save_personrelation_offline),
    (r'^dashboard/getpersonmeetingattendancesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personmeetingattendances_online),
    (r'^dashboard/savepersonmeetingattendanceoffline/((?P<id>\d*)/)?$', save_personmeetingattendance_offline),
    (r'^dashboard/savepersonadoptpracticeonline/((?P<id>\d*)/)?$', save_personadoptpractice_online),
    (r'^dashboard/getpersonadoptpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_personadoptpractices_online),
    (r'^dashboard/savepersonadoptpracticeoffline/((?P<id>\d*)/)?$', save_personadoptpractice_offline),
    (r'^dashboard/saveequipmentholderonline/$', save_equipmentholder_online),
    (r'^dashboard/getequipmentholdersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_equipmentholders_online),
    (r'^dashboard/saveequipmentholderoffline/((?P<id>\d*)/)?$', save_equipmentholder_offline),
    (r'^dashboard/saverevieweronline/$', save_reviewer_online),
    (r'^dashboard/getreviewersonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_reviewers_online),
    (r'^dashboard/saverevieweroffline/((?P<id>\d*)/)?$', save_reviewer_offline),
    (r'^dashboard/savetargetonline/((?P<id>\d*)/)?$', save_target_online),
    (r'^dashboard/gettargetsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_targets_online),
    (r'^dashboard/savetargetoffline/((?P<id>\d*)/)?$', save_target_offline),
    (r'^dashboard/geterrorsonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$',get_dashboard_errors_online),
    (r'^dashboard/notanerror/((?P<offset>\d*)/(?P<limit>\d*)/)?$',mark_error_as_not_error),
    (r'^dashboard/getindexdata/$',index_template_data),
    (r'^dashboard/personsingroup/$',farmers_in_groups),
    (r'^dashboard/personsinscreening/((?P<screening_id>\d*)/)?$',persons_in_screening),
    (r'^dashboard/personmeetingattendance/(?P<person_id>\d*)/(?P<screening_id>\d*)', person_meeting_attendance_data),
    (r'^dashboard/screeningsinvillage/((?P<village_id>\d*)/)?$',screenings_in_village),
    (r'^dashboard/filtereddataforvillage/((?P<village_id>\d*)/)?$', filters_for_village),
    (r'^dashboard/practicesforperson/((?P<person_id>\d*)/)?$', practices_seen_by_farmer),
    (r'^dashboard/practicesinvideos/$', practices_in_videos),
    (r'^$',home),
    (r'^farmerbook/$', farmer_book_views.get_home_page),
    (r'^farmerbook/(?P<type>\D*)/(?P<id>\d*)/$', farmer_book_views.get_home_page),
    (r'^trial/?$', farmer_book_views.get_admin_panel),
    (r'^getvillagepage/?$', farmer_book_views.get_village_page),
    (r'^getserviceproviderpage/?$', farmer_book_views.get_csp_page),
    (r'^getpartnerpage/?$', farmer_book_views.get_partner_page),
    (r'^getpersonpage/?$', farmer_book_views.get_person_page),
    (r'^getgrouppage/?$', farmer_book_views.get_group_page),
    (r'^getvillages/?$', farmer_book_views.get_villages_with_images),
    (r'^getvideosproduced/?$', farmer_book_views.get_videos_produced),
    (r'^videotask/', include('video_practice_map.urls')),    
    (r'^home/?$',home),
    (r'^wondervillage/?$',wondervillage),
    (r'^wondervillagegame/?$',wondervillagegame),
    (r'^annualreports/?$',annualreports),
    (r'^featuredfarmer/?$',featuredfarmer),
    (r'^melissaho/?$',melissaho),
    (r'^aishwaryaratan/?$',aishwaryaratan),
    (r'^srikantvasan/?$',srikantvasan),
    (r'^videopage/?$',videopage),
    (r'^searchvideo_result/?$',searchvideo_result),
    (r'^aboutus/?$',aboutus),
    (r'^annualreport09/?$',annualreport09),
    (r'^annualreport10/?$',annualreport10),
    (r'^annualreport10pdf/?$',annualreport10pdf),
    (r'^annualletter/?$',annualletter),
    (r'^annualletter10/?$',annualletter10),
    (r'^projectprogress/?$',projectprogress),
    (r'^projectprogress10/?$',projectprogress10),
    (r'^partners10/?$',partners10),
    (r'^budgetprogress/?$',budgetprogress),
    (r'^financial10/?$',financial10),
    (r'^scalability/?$',scalability),
    (r'^lessonlearned/?$',lessonlearned),
    (r'^challenge10/?$',challenge10),
    (r'^keyprinciple/?$',keyprinciple),
    (r'^corevalue/?$',corevalue),
    (r'^sop/?$',sop),
    (r'^qualityassurance/?$',qualityassurance),
    (r'^overviewfarmer/?$',overviewfarmer),
    (r'^overviewdatabase/?$',overviewdatabase),
    (r'^overviewproduction/?$',overviewproduction),
    (r'^overviewsequence/?$',overviewsequence),
    (r'^overviewdiffusion/?$',overviewdiffusion),
    (r'^overviewscalability/?$',overviewscalability),
    (r'^overviewdistribution/?$',overviewdistribution),
    (r'^career/?$',career),
    (r'^careers/?$',careers),
    (r'^contact/?$',contact),
    (r'^team/?$',team),
    (r'^teamboard/?$',teamboard),
    (r'^teamadviser/?$',teamadviser),
    (r'^teamacclaw/?$',teamacclaw),
    (r'^teamintern/?$',teamintern),
    (r'^teamalumni/?$',teamalumni),
    (r'^teammember/?$',teammember),
    (r'^press/?$',press),
    (r'^partner/?$',partner),
    (r'^rfa/?$',rfa),
    (r'^partnerexecutive/?$',partnerexecutive),
    (r'^partnerresearch/?$',partnerresearch),
    (r'^partnerinvestor/?$',partnerinvestor),
    (r'^partnersupporter/?$',partnersupporter),
    (r'^careerid/?$',careerid),
    (r'^careersm/?$',careersm),
    (r'^careerpm/?$',careerpm),
    (r'^careernm/?$',careernm),
    (r'^careerpca/?$',careerpca),
    (r'^careernpc/?$',careernpc),
    (r'^careerts/?$',careerts),
    (r'^careerqam/?$',careerqam),
    (r'^careerrse/?$',careerrse),
    (r'^careeradm/?$',careeradm),
    (r'^donate/?$',donate),
    (r'^tech/?$',tech),
    (r'^photos/?$',photos),
    (r'^webvideos/?$',webvideos),
    (r'^keyfacts/?$',keyfacts),
    (r'^farmerpage/?$',farmerpage),
    (r'^villagepage/?$',villagepage),
    (r'^grouppage/?$',grouppage),
    (r'^retreat11/?$',retreat11),
    (r'^update/?$',update),
    (r'^latestupdate/?$',latestupdate),
    (r'^nexus/?$',nexus),
    (r'^analytics/overview_module/?$',overview_analytics.overview_module),
    (r'^analytics/get_parent_geog_id/?$',overview_analytics.get_parent_geog_id),
    (r'^analytics/screening_module/?$',screening_analytics.screening_module),
    (r'^analytics/screening_tot_lines/?$',screening_analytics.screening_tot_lines),
    (r'^analytics/screening_percent_lines/?$',screening_analytics.screening_percent_lines),
    (r'^analytics/screening_per_day_line/?$',screening_analytics.screening_per_day_line),
    (r'^analytics/screening_monthwise_bar_data/?$',screening_analytics.screening_monthwise_bar_data),
    (r'^analytics/screening_practice_wise_scatter_data/?$',screening_analytics.screening_practice_wise_scatter_data),
    (r'^analytics/screening_mf_ratio/?$',screening_analytics.screening_mf_ratio),
    (r'^analytics/screening_geog_pie_data/?$',screening_analytics.screening_geog_pie_data),
    (r'^analytics/get_dist_attendees_avg_att_avg_sc/?$',screening_analytics.get_dist_attendees_avg_att_avg_sc),
    (r'^analytics/video_module/?$',video_analytics.video_module),
    (r'^analytics/video_pie_graph_mf_ratio/?$',video_analytics.video_pie_graph_mf_ratio),
    (r'^analytics/video_actor_wise_pie/?$',video_analytics.video_actor_wise_pie),
    (r'^analytics/video_type_wise_pie/?$',video_analytics.video_type_wise_pie),
    (r'^analytics/video_geog_pie_data/?$',video_analytics.video_geog_pie_data),
    (r'^analytics/video_language_wise_scatter_data/?$',video_analytics.video_language_wise_scatter_data),
    (r'^analytics/video_practice_wise_scatter/?$',video_analytics.video_practice_wise_scatter),
    (r'^analytics/video_monthwise_bar_data/?$',video_analytics.video_monthwise_bar_data),
    (r'^video/?$',video_analytics.video),
    (r'^analytics/video_search/?$',video_analytics.video_search),
    (r'^analytics/video_screening_month_bar_data/?$',video_analytics.video_screening_month_bar_data),
    (r'^analytics/adoption_module/?$',adoption_analytics.adoption_module),
    (r'^analytics/adoption_pie_graph_mf_ratio/?$',adoption_analytics.adoption_pie_graph_mf_ratio),
    (r'^analytics/adoption_geog_pie_data/?$',adoption_analytics.adoption_geog_pie_data),
    (r'^analytics/adoption_practice_wise_scatter/?$',adoption_analytics.adoption_practice_wise_scatter),
    (r'^analytics/adoption_monthwise_bar_data/?$',adoption_analytics.adoption_monthwise_bar_data),
    (r'^analytics/adoption_rate_line/?$',adoption_analytics.adoption_rate_line),
    (r'^analytics/target_table/?$',targets.target_table),
    (r'^analytics/drop_down_val/?$',drop_down_val),
    (r'^analytics/overview_line_graph/?$',overview_line_graph),
    (r'^analytics/practice_change/?$',practice_change),
    #Remove once Farmerbook video url's are fixed 
    (r'^analytics/video/?$',video_analytics.video),
    (r'^path/page/?$',page),
    (r'^path/update/?$',update),
    (r'^fbconnect/', include('fbconnect.urls')),
    (r'^get_log/?$',send_updated_log),
     
)

# Static files serving locally
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
