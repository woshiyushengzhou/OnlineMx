# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-12 17:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7ae0\u8282\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=40, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('courseIntroduction', models.TextField(verbose_name='\u8bfe\u7a0b\u7b80\u4ecb')),
                ('courseDegree', models.CharField(choices=[('chuji', '\u521d\u7ea7'), ('zhongji', '\u4e2d\u7ea7'), ('gaoji', '\u9ad8\u7ea7')], max_length=10, verbose_name='\u8bfe\u7a0b\u96be\u5ea6')),
                ('courseTime', models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u65f6\u957f')),
                ('students', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570')),
                ('chapters', models.SmallIntegerField(default=0, verbose_name='\u8bfe\u7a0b\u7ae0\u8282\u6570')),
                ('category', models.CharField(max_length=30, verbose_name='\u8bfe\u7a0b\u7c7b\u522b')),
                ('click_nums', models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u70b9\u51fb\u6570')),
                ('courseCover', models.ImageField(upload_to='courses/%Y/%m', verbose_name='\u8bfe\u7a0b\u5c01\u9762')),
                ('collect_nums', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4eba\u6570')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u8bfe\u7a0b\u52a0\u5165\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u8d44\u6e90\u540d\u79f0')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='\u4e0b\u8f7d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b')),
            ],
            options={
                'verbose_name': '\u8d44\u6e90',
                'verbose_name_plural': '\u8d44\u6e90',
            },
        ),
        migrations.CreateModel(
            name='Viedo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u89c6\u9891\u540d\u79f0')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Chapter', verbose_name='\u7ae0\u8282')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b\u540d\u79f0'),
        ),
    ]
