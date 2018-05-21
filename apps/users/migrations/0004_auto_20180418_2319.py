# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-18 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '\u8f6e\u64ad\u56fe', 'verbose_name_plural': '\u8f6e\u64ad\u56fe'},
        ),
        migrations.AlterModelOptions(
            name='userporfile',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AlterField(
            model_name='userporfile',
            name='gender',
            field=models.CharField(choices=[('man', '\u7537\u6027'), ('woman', '\u5973\u6027')], max_length=5, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='userporfile',
            name='phone_num',
            field=models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7'),
        ),
    ]
