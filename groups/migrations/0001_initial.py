# Generated by Django 5.1.4 on 2025-01-02 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(max_length=100)),
                ('class_leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='teachers.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]