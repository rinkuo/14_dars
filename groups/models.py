from django.db import models
from teachers.models import Teacher
from .base_model import BaseModel
from django.shortcuts import reverse


class Group(BaseModel):
    class_leader = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='leader')
    group_name = models.CharField(max_length=100)
    students = models.ManyToManyField('students.Student', blank=True, related_name='group_of_students')

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def __str__(self):
        return f"{self.class_leader} - {self.group_name}"