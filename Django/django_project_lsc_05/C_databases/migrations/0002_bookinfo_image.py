# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-26 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C_databases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='adata', verbose_name='图片'),
        ),
    ]
