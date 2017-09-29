from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.safestring import mark_safe
import os

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

    def as_dict(self):
        return {
            'link': self.link,
            'year': self.year
        }

    class Meta:
        verbose_name = "Historical Aerial Link"
        verbose_name_plural = "Historical Aerial Links"


def get_upload_path(instance, filename):
    return os.path.join(str(instance.lake), filename)


class StoryContent(models.Model):
    lake = models.OneToOneField(MajorReservoirs, primary_key=True)
    summary = models.TextField()
    history = models.TextField()

    section_one_nav = models.CharField(max_length=25, blank=True)
    section_one_header = models.CharField(max_length=50, blank=True)
    section_one_content = models.TextField(blank=True)
    section_one_photo = models.ImageField(upload_to=get_upload_path,
                                          blank=True)

    section_two_nav = models.CharField(max_length=25, blank=True)
    section_two_header = models.CharField(max_length=50, blank=True)
    section_two_content = models.TextField(blank=True)

    section_three_nav = models.CharField(max_length=25, blank=True)
    section_three_header = models.CharField(max_length=50, blank=True)
    section_three_content = models.TextField(blank=True)

    # def save(self, *args, **kwargs):
    #     self.section_one_nav = self.section_one_nav.lower().replace(" ", "")
    #     super().save(*args, **kwargs)  # Call the "real" save() method.

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />'
                         % (self.section_one_photo))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "Story Content"
        verbose_name_plural = "Story Content"
