# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0032_auto_20190613_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalaeriallinks',
            name='datahub_collection_id',
            field=models.CharField(blank=True, default='', max_length=36),
        ),
    ]
