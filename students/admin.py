from django.contrib import admin
from .models import Student
from groups.models import Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'phone_number', 'birth_date')
    search_fields = ['first_name', 'last_name', 'phone_number']
    list_filter = ('group',)
    list_editable = ('group',)
    readonly_fields = ('birth_date',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'phone_number', 'address')
        }),
        ('Group and Birth Date', {
            'fields': ('group', 'birth_date'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Student, StudentAdmin)
