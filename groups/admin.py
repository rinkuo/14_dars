from django.contrib import admin
from .models import Group
from teachers.models import Teacher


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'class_leader', 'get_students_count')
    search_fields = ['group_name']
    list_filter = ('class_leader',)
    ordering = ['group_name']
    filter_horizontal = ('students',)
    readonly_fields = ('class_leader',)

    def get_students_count(self, obj):
        return obj.students.count()

    get_students_count.short_description = 'Number of Students'

    class StudentsInline(admin.TabularInline):
        model = Group.students.through
        extra = 1

    inlines = [StudentsInline]


admin.site.register(Group, GroupAdmin)
