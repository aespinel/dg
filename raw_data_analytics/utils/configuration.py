__author__ = 'Lokesh'

tableDictionary={
    'partner':'programs_partner',
    'country':'geographies_country',
    'state':'geographies_state',
    'district':'geographies_district',
    'block':'geographies_block',
    'village':'geographies_village',
    'animator':'people_animatorwisedata',
    'person':'people_person',
    'persongroup':'people_persongroup',
    'video':'videos_video_wisedata',
    'language':'videos_language',
    'sector':'videos_practicesector',
    'practice':'videos_practice',
    'topic':'videos_practicetopic',
    'numScreening':'activities_screeningwisedata',
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':'activities_personadoptpractice',
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':'activities_pmawisedata',
    'numPeople':'people_person',
    'numAnimator':'people_animatorwisedata',
    'listPeople':'people_person',
    'listAnimator':'people_animatorwisedata',
    'listVideoScreened':'activities_screeningwisedata',
    'numVideoScreened':'activities_screeningwisedata',
    'listVideoProduced':'videos_video_wisedata',
    'numVideoProduced':'videos_video_wisedata',
    'list':'self',
    'listGroup':'people_persongroup'
}

whereDictionary={
    'partner':'id',
    'country':'id',
    'state':'id',
    'district':'id',
    'block':'id',
    'village':'id',
    'animator':'animator_id',
    'person':'id',
    'persongroup':'id',
    'video':'id',
    'language':'id',
    'sector':'id',
    'practice':'id',
    'topic':'id',
    'numScreening':'screening_date',
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':'date_of_adoption',
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':'time_created',
    'numPeople':'time_created',
    'numAnimator':'time_created',
    'listPeople':'time_created',
    'listAnimator':'time_created',
    'listVideoScreened':'screening_date',
    'numVideoScreened':'screening_date',
    'listVideoProduced':'video_production_end_date',
    'numVideoProduced':'video_production_end_date',
    'list':'self',
    'listGroup':'time_created'
}


categoryDictionary={
    'geographies':['country','state','district','block','village'],
    'partitionCumValues':{'listAnimator':'animator','listVideoScreened':'video','listVideoProduced':'video','listPeople':'person','listGroup':'persongroup','numScreening':'numScreening'},
    'numAdoptionClub':['animator','persongroup','video','person'],
    'attendanceClub':['animator','video','persongroup','person']
}

groupbyDictionary={
    'partner':'id',
    'country':'id',
    'state':'id',
    'district':'id',
    'block':'id',
    'village':'id',
    'animator':'animator_id',
    'person':'id',
    'persongroup':'id',
    'video':'id',
    'language':'id',
    'sector':'id',
    'practice':'id',
    'topic':'id',
    'numScreening':False,
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':False,
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':False,
    'numPeople':False,
    'numAnimator':False,
    'listPeople':'id',
    'listAnimator':'animator_id',
#    'listVideoScreened':'video_id',
    'numVideoScreened':False,
#    'listVideoProduced':'video_id',
    'numVideoProduced':False,
    'list':'self',
    'listVideoProduced':'video_id',
    'listVideoScreened':'video_id',
    'listGroup':'id'
}

selectDictionary={
    'partner':{'id':False,'partner_name':True},
    'country':{'id':False,'country_name':True},
    'state':{'id':False,'state_name':True},
    'district':{'id':False,'district_name':True},
    'block':{'id':False,'block_name':True},
    'village':{'id':False,'village_name':True},
    'animator':{'animator_id':False,'animator_name':True,'gender':False},
    'person':{'id':False,'person_name':True,'gender':True},
    'persongroup':{'id':False,'group_name':True},
    'video':{'id':False,'title':True},
    'language':{'id':False,'language_name':True},
    'sector':{'id':False,'name':True},
    'practice':{'id':False,'practice_name':True},
    'topic':{'id':False,'name':True},
    'numScreening':{'count(screening_id)':True,'count(distinct screening_id)':False},
#    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
#    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
    'numAdoption':{'count(id)':True,'count(distinct person_id)':False},
#    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
#    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
    'attendance':{'count(pma_id)':True,'count(distinct pma_id)':False},
    'numPeople':{'count(id)':True,'count(distinct id)':False},
    'numAnimator':{'count(id)':True,'count(distinct id)':False},
    'listPeople':{'person_name':True,'gender':False},
    'listAnimator':{'animator_name':True,'gender':False},
#    'listVideoScreened':{'id':False,'video_title':True},
    'numVideoScreened':{'count(video_id)':True,'count(distinct id)':False},
#    'listVideoProduced':{'id':False,'title':True},
    'numVideoProduced':{'count(id)':True,'count(distinct id)':False},
    'list':'self',
    'listVideoProduced':{'id':False,'title':True},
    'listVideoScreened':{'id':False,'video_title':True},
    'listGroup':{'id':False,'group_name':True}
}


#
# generalDictionary = {
#     'partner':{'table':'programs_partner','column':'partner_name','function':'partner_func()'},
#     'country':{'table':'geographies_country','column':'country_name','function':'country_func()'},
#     'state':{'table':'geographies_state','column':'state_name','function':'state_func()'},
#     'district':{'table':'geographies_district','column':'district_name','function':'district_func()'},
#     'block':{'table':'geographies_block','column':'block_name','function':'block_func()'},
#     'village':{'table':'geographies_village','column':'village_name','function':'village_func()'},
#     'animator':{'table':'people_animator_wise_data','column':'animator_name','function':'animator_func()'},
#     'person':{'table':'people_person','column':'person_name','function':'person_func()'},
#     'persongroup':{'table':'people_persongroup','column':'group_name_name','function':'persongroup_func()'},
#     'video':{'table':'videos_video_wise_data','column':'title','function':'video_func()'},
#     'language':{'table':'videos_language','column':'language_name','function':'language_func()'},
#     'sector':{'table':'videos_practicesector','column':'name','function':'practicesector_func()'},
#     'practice':{'table':'videos_practice','column':'practice_name','function':'practice_func()'},
#     'numScreening':{'table':'people_animator_wise_data','column':'nScreenings','function':'animator_screening_func()'},
# #    'video_n_screening':{'table':'videos_video_wise_data','column':'nScreenings','function':'video_screening_func()'},
# #    'person_n_screening':{'table':'people_person_wise_data','column':'nScreenings','function':'person_screening_func()'},
#     'numAdoption':{'table':'people_animator_wise_data','column':'nAdoptions','function':'animator_adoption_func()'},
# #    'video_n_adoption':{'table':'videos_video_wise_data','column':'nAdoptions','function':'video_adoption_func()'},
# #    'person_n_adoption':{'table':'people_person_wise_data','column':'nAdoptions','function':'person_adoption_func()'},
#     'screening':{'table':'activities_screening','column':'id','function':'screening_func()'},
#     'adoption':{'table':'activities_personadoptpractice','column':'id','function':'adoption_func()'},
#     'meetingAttendance':{'table':'activities_personmeetingattendance','column':'id','function':'meetingAttendance_func()'},
#     'adoption':{'table':'activities_personadoptpractice','column':'id','function':'adoption_func()'},
#
# }
#
