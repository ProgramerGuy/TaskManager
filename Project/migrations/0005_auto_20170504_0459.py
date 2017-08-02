# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-04 04:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
        ('Project', '0004_auto_20170504_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.AddField(
            model_name='project',
            name='project_users',
            field=models.ManyToManyField(blank=True, related_name='project_users', to='UserProfile.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserProfile.Profile'),
        ),
    ]
