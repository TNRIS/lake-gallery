# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import map.validators


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0027_majorreservoirs_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='lakestatistics',
            name='wdft_link',
            field=models.URLField(help_text='WDFT lake page link. Ex: https://waterdatafortexas.org/reservoirs/individual/<lake name>', null=True),
        ),
        migrations.AlterField(
            model_name='significantevents',
            name='date',
            field=models.DateField(validators=[map.validators.validate_past_dates]),
        ),
    ]