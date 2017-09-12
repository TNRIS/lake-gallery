# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 19:32
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajorReservoirs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('res_lbl', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='RWPAs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('reg_name', models.CharField(max_length=25)),
                ('letter', models.CharField(max_length=1)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
