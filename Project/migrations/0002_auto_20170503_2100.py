# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-03 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PriorityTask',
            new_name='TaskPriority',
        ),
    ]
