# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import map.validators


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0023_auto_20171009_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lakestatistics',
            name='historic_high_date',
            field=models.DateField(blank=True, null=True, validators=[map.validators.validate_past_dates]),
        ),
        migrations.AlterField(
            model_name='lakestatistics',
            name='historic_low_date',
            field=models.DateField(blank=True, null=True, validators=[map.validators.validate_past_dates]),
        ),
    ]
