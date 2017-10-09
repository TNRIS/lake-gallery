from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.safestring import mark_safe
from multiselectfield import MultiSelectField
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
    history_photo = models.ImageField(upload_to=get_upload_path,
                                      blank=True)

    section_one_nav = models.CharField(max_length=25, blank=True)
    section_one_header = models.CharField(max_length=50, blank=True)
    section_one_content = models.TextField(blank=True)
    section_one_photo = models.ImageField(upload_to=get_upload_path,
                                          blank=True)

    section_two_nav = models.CharField(max_length=25, blank=True)
    section_two_header = models.CharField(max_length=50, blank=True)
    section_two_content = models.TextField(blank=True)
    section_two_photo = models.ImageField(upload_to=get_upload_path,
                                          blank=True)

    section_three_nav = models.CharField(max_length=25, blank=True)
    section_three_header = models.CharField(max_length=50, blank=True)
    section_three_content = models.TextField(blank=True)
    section_three_photo = models.ImageField(upload_to=get_upload_path,
                                            blank=True)

    # def save(self, *args, **kwargs):
    #     self.section_one_nav = self.section_one_nav.lower().replace(" ", "")
    #     super().save(*args, **kwargs)  # Call the "real" save() method.

    def hist_tag(self):
        return mark_safe('<img src="/media/%s" style="max-height:150px;" />'
                         % (self.history_photo))
    hist_tag.allow_tags = True

    def one_tag(self):
        return mark_safe('<img src="/media/%s" style="max-height:150px;" />'
                         % (self.section_one_photo))
    one_tag.allow_tags = True

    def two_tag(self):
        return mark_safe('<img src="/media/%s" style="max-height:150px;" />'
                         % (self.section_two_photo))
    two_tag.allow_tags = True

    def three_tag(self):
        return mark_safe('<img src="/media/%s" style="max-height:150px;" />'
                         % (self.section_three_photo))
    three_tag.allow_tags = True

    class Meta:
        verbose_name = "Story Content"
        verbose_name_plural = "Story Content"


class LakeStatistics(models.Model):
    purpose_choices = (('Flood Management', 'Flood Management'),
                       ('Water Storage', 'Water Storage'),
                       ('Hydroelectric Power', 'Hydroelectric Power'))

    lake = models.OneToOneField(MajorReservoirs, primary_key=True)

    # general stats
    original_name = models.CharField(max_length=50, blank=True)
    primary_purposes = MultiSelectField(choices=purpose_choices, null=True,
                                        blank=True)
    location = models.CharField(max_length=50, blank=True,
                                help_text="Ex. Travis County, Texas")
    construction_dates = models.CharField(max_length=50, blank=True,
                                          help_text="Ex. 1937 to 1942")
    length_of_lake = models.FloatField(default=0, blank=True,
                                       help_text="Miles")
    miles_of_shoreline = models.FloatField(default=0, blank=True,
                                           help_text="Miles")
    maximum_width = models.FloatField(default=0, blank=True, help_text="Miles")
    lake_area = models.FloatField(default=0, blank=True, help_text="Acres")
    lake_capacity = models.FloatField(default=0, blank=True,
                                      help_text="Acre-feet")
    full_elevation_msl = models.FloatField(default=0, blank=True,
                                           help_text="Mean Sea Level")
    full_elevation_gal = models.FloatField(default=0, blank=True,
                                           help_text="Gallons of Water")
    maximum_depth = models.FloatField(default=0, blank=True, help_text="Feet")
    average_depth = models.FloatField(default=0, blank=True, help_text="Feet")
    historic_high_msl = models.FloatField(default=0, blank=True,
                                          help_text="Feet above Mean Sea"
                                          " Level")
    historic_high_date = models.DateField(null=True, blank=True)
    historic_low_msl = models.FloatField(default=0, blank=True,
                                         help_text="Feet above Mean Sea Level")
    historic_low_date = models.DateField(null=True, blank=True)

    # dam stats
    dam_height = models.FloatField(default=0, blank=True, help_text="Feet")
    dam_width = models.FloatField(default=0, blank=True, help_text="Feet")
    spillway_elevation = models.FloatField(default=0, blank=True,
                                           help_text="Feet above Mean Sea"
                                           " Level")
    top_of_dam = models.FloatField(default=0, blank=True,
                                   help_text="Feet above Mean Sea Level")
    num_of_floodgates = models.PositiveIntegerField(default=0, blank=True,
                                                    verbose_name='Number of '
                                                    'Floodgates')
    discharge_capacity = models.TextField(blank=True, help_text="typically - "
                                          "Cubic Feet per Second")

    def string_numbers(self):
        flds = self._meta.get_fields()
        for f in flds:
            field_type = f.get_internal_type()
            if field_type == 'FloatField':
                attr = getattr(self, f.name)
                string = "{:,}".format(attr)
                if string[-2:] == ".0":
                    string = string[:-2]
                setattr(self, f.name, string)
        return self

    def set_displays(self):
        self.stat_defaults = [0.0, 0, "0.0", "", None, "None"]
        self.primary_purposes = str(self.primary_purposes)
        self.general_stats = False
        general_stats = [self.original_name,
                         self.primary_purposes,
                         self.location,
                         self.construction_dates,
                         self.length_of_lake,
                         self.miles_of_shoreline,
                         self.maximum_width,
                         self.lake_area,
                         self.lake_capacity,
                         self.full_elevation_msl,
                         self.full_elevation_gal,
                         self.maximum_depth,
                         self.average_depth,
                         self.historic_high_msl,
                         self.historic_high_date,
                         self.historic_low_msl,
                         self.historic_low_date]
        for g in general_stats:
            if g not in self.stat_defaults:
                self.general_stats = True

        self.dam_stats = False
        dam_stats = [self.dam_height,
                     self.dam_width,
                     self.spillway_elevation,
                     self.top_of_dam,
                     self.num_of_floodgates,
                     self.discharge_capacity]
        for d in dam_stats:
            if d not in self.stat_defaults:
                self.general_stats = True
                self.dam_stats = True
        return self

    class Meta:
        verbose_name = "Lake Statistics"
        verbose_name_plural = "Lake Statistics"


class SignificantEvents(models.Model):
    lake = models.ForeignKey(MajorReservoirs)
    event_type = models.CharField(max_length=4,
                                  choices=[('High', 'High'), ('Low', 'Low')],
                                  default='High')
    date = models.DateField()
    height = models.FloatField(help_text="Feet above mean sea level")
    drought = models.CharField(max_length=9, blank=True,
                               help_text="Year range of drought (low "
                               "events only). Example: '1947-57'")

    def __str__(self):
        return self.event_type + " " + str(self.date)

    class Meta:
        verbose_name = "Significant Event"
        verbose_name_plural = "Significant Events"
