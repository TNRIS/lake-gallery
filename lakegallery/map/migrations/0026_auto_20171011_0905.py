# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0025_boatramps_channelmarkers_hazards_parks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazards',
            name='hazard_type',
            field=models.CharField(choices=[('Hazard', 'Hazard'), ('No Boats', 'No Boats'), ('No Wake', 'No Wake'), ('Rocks', 'Rocks')], default='Hazard', max_length=35),
        ),
    ]