# Generated by Django 5.1.4 on 2025-01-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_students'),
        ('teachers', '0002_alter_teacher_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='groups.group'),
        ),
    ]
