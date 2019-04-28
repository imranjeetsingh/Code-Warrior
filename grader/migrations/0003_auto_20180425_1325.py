# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-25 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0002_auto_20180424_0227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solution',
            options={'ordering': ['-score', 'total_time']},
        ),
        migrations.AddField(
            model_name='solution',
            name='total_time',
            field=models.IntegerField(default=0),
        ),
    ]