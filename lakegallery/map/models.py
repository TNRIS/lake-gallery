from django.db import models
from django.contrib.gis.db import models as gismodels

import datetime
YEAR_CHOICES = []
for r in range(1920, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class MajorReservoirs(gismodels.Model):
    res_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    res_lbl = models.CharField(max_length=100)
    region = models.CharField(max_length=1)

    geom = gismodels.MultiPolygonField(srid=4326)
    objects = gismodels.GeoManager()

    def __str__(self):
        return self.res_lbl

    class Meta:
        verbose_name = "Major Reservoir"
        verbose_name_plural = "Major Reservoirs"


class RWPAs(gismodels.Model):
    objectid = models.BigIntegerField()
    reg_name = models.CharField(max_length=25)
    letter = models.CharField(max_length=1)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = gismodels.MultiPolygonField(srid=4326)
    objects = gismodels.GeoManager()

    def __str__(self):
        return self.reg_name

    class Meta:
        verbose_name = "RWPA"
        verbose_name_plural = "RWPAs"


class HistoricalAerialLinks(models.Model):
    link = models.URLField()
    year = models.IntegerField(choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)
    lake = models.ForeignKey(MajorReservoirs)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = "Historical Aerial Link"
        verbose_name_plural = "Historical Aerial Links"
