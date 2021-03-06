from django.contrib import admin

class XMLSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'error_code', 'error_message', 'submission_time', 'xml_data')
    search_fields = ['username', 'xml_data', 'error_code', 'error_message']

class CommCareProjectAdmin(admin.ModelAdmin):
    fieldsets = [(None,  {'fields': ['name']
                          }
                  )]
    list_display = ('name',)
    search_fields = ['name']


class CommCareUserAdmin(admin.ModelAdmin):
    fieldsets = [(None,  {'fields': ['username', 'guid', 'project', 'is_user', 'coco_user']
                          }
                  )]
    list_display = ('username', 'project', 'guid', 'is_user')
    search_fields = ['username']


class CommCareUserVillageAdmin(admin.ModelAdmin):
    fieldsets = [(None,  {'fields': ['user', 'village']
                          }
                  )]
    list_display = ('user', 'village')
    search_fields = ['user']


class CommCareCaseAdmin(admin.ModelAdmin):
    fieldsets = [(None,  {'fields': ['person', 'guid', 'project', 'user', 'is_open']
                          }
                  )]
    list_display = ('person', 'guid', 'is_open')
