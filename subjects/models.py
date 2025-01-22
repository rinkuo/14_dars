from django.db import models
from django.shortcuts import reverse
from groups.base_model import BaseModel

class Subject(BaseModel):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('teachers.Teacher', related_name='assigned_subjects', blank=True)

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def __str__(self):
        return self.name

    @property
    def teachers_count(self):
        return self.teachers.count()
