# Generated by Django 5.1.4 on 2025-01-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='teachers.teacher'),
        ),
    ]
