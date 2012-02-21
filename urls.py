from django.conf.urls.defaults import *
from route import route
from django.conf.urls.defaults import *
from views import *
from django.contrib.auth.views import login, logout
from django.conf import settings
from static_site_views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^coco/', redirect_url),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
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
    (r'^dashboard/getvideorelatedagriculturalpracticesonline/((?P<offset>\d*)/(?P<limit>\d*)/)?$', get_videoagriculturalpractices_online),
    (r'^dashboard/savevideorelatedagriculturalpracticesonline/$', save_videoagriculturalpractices_online),
    (r'^dashboard/savevideorelatedagriculturalpracticesoffline/((?P<id>\d*)/)?$', save_videoagriculturalpractices_offline),
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
    (r'^dashboard/savescreeningfarmergroupstargetedsonline/$',save_groupstargetedinscreening_online),
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
    (r'^dashboard/savepersonmeetingattendanceonline/$', save_personmeetingattendance_online),
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
    (r'^(?P<func_name>.*)/$',route),  #Routing call
)
