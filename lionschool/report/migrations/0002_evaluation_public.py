# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lionreport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='public',
            field=models.BooleanField(default=False, verbose_name='public'),
        ),
    ]
