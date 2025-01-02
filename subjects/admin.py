from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Subject, SubjectAdmin)