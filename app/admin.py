from django.contrib import admin
from .models import Project, Stage, Task, Report, UserProject, UserStage, UserTask

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'describe', 'start_date', 'end_date', 'status', 'deleted_at')
    search_fields = ('name', 'describe')

class StageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'project')
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'start_date', 'end_date', 'status', 'stage_id', 'user')
    search_fields = ('content',) 


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'start_date', 'end_date', 'status', 'stage_id')
    search_fields = ('content',) 
   



    


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'user', 'project')
    search_fields = ('content',)

# Đăng ký các mô hình với lớp admin tương ứng
admin.site.register(Project, ProjectAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(UserProject)
admin.site.register(UserStage)
admin.site.register(UserTask)
