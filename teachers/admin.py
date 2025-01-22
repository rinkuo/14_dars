from django.contrib import admin
from .models import Teacher
from subjects.models import Subject

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'phone_number', 'work_experience')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('subject',)
    readonly_fields = ('work_experience',)
    ordering = ['last_name']
    filter_horizontal = ('groups',)

    def reset_experience(self, request, queryset):
        queryset.update(work_experience=0)
    reset_experience.short_description = 'Reset Work Experience to 0'

    actions = [reset_experience]

admin.site.register(Teacher, TeacherAdmin)
