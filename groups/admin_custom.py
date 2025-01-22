from django.contrib.admin import AdminSite
from .models import Group
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from .admin import GroupAdmin

class MyAdminSite(AdminSite):
    site_header = "Mening Custom Admin Panelim"
    site_title = "Admin Panel"
    index_title = "Custom Admin Panelga Xush Kelibsiz"

admin_site = MyAdminSite(name='myadmin')

admin_site.register(Group, GroupAdmin)
admin_site.register(Student)
admin_site.register(Teacher)
admin_site.register(Subject)
