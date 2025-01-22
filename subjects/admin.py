from django.contrib import admin
from .models import Subject
from teachers.models import Teacher

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teachers_count')
    search_fields = ['name']
    list_filter = ('teachers',)
    ordering = ['name']

    def teachers_count(self, obj):
        return obj.teachers.count()
    teachers_count.short_description = 'Number of Teachers'

admin.site.register(Subject, SubjectAdmin)
