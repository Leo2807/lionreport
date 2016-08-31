# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 11:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lioncore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('desc', models.TextField(blank=True, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lioncore.Course', verbose_name='course')),
            ],
            options={
                'verbose_name_plural': 'evaluations',
                'verbose_name': 'evaluation',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='score')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
                ('evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lionreport.Evaluation', verbose_name='evaluation')),
                ('pupil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lioncore.Pupil', verbose_name='pupil')),
            ],
            options={
                'verbose_name_plural': 'results',
                'verbose_name': 'result',
            },
        ),
    ]
