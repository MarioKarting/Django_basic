# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-26 02:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('B_test', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
    ]
