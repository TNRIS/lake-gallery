from django.db import models
from django.contrib.gis.db import models as gismodels


class MajorReservoirs(gismodels.Model):
    res_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    res_lbl = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

    geom = gismodels.MultiPolygonField(srid=4326)
    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.res_name


class RWPAs(gismodels.Model):
    objectid = models.BigIntegerField()
    reg_name = models.CharField(max_length=25)
    letter = models.CharField(max_length=1)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()

    geom = gismodels.MultiPolygonField(srid=4326)
    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.reg_name
