# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-26 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_course_org'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='chapters',
        ),
    ]
