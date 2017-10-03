from django.contrib.gis import admin
from .models import (MajorReservoirs, RWPAs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics)


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')


class StoryContentAdmin(admin.ModelAdmin):
    list_display = ['lake']
    fieldsets = [
        (None,               {'fields': ['lake', 'summary', 'history',
                                         ('history_photo', 'hist_tag')]}),
        ('Additional Section 1', {'fields': ['section_one_nav',
                                             'section_one_header',
                                             'section_one_content',
                                             ('section_one_photo',
                                              'one_tag')]}),
        ('Additional Section 2', {'fields': ['section_two_nav',
                                             'section_two_header',
                                             'section_two_content',
                                             ('section_two_photo',
                                              'two_tag')]}),
        ('Additional Section 3', {'fields': ['section_three_nav',
                                             'section_three_header',
                                             'section_three_content',
                                             ('section_three_photo',
                                              'three_tag')]}),
    ]
    readonly_fields = ('hist_tag', 'one_tag', 'two_tag', 'three_tag')


class LakeStatisticsAdmin(admin.ModelAdmin):
    list_display = ['lake']
    fieldsets = [
        (None, {'fields': ['lake']}),
        ('General Statistics', {'fields': ['original_name',
                                           'primary_purposes',
                                           'location',
                                           'construction_dates',
                                           'length_of_lake',
                                           'miles_of_shoreline',
                                           'maximum_width',
                                           'lake_area',
                                           'lake_capacity',
                                           'full_elevation_msl',
                                           'full_elevation_gal',
                                           'maximum_depth',
                                           'average_depth',
                                           'historic_high_msl',
                                           'historic_high_date',
                                           'historic_low_msl',
                                           'historic_low_date']}),
        ('Dam Statistics', {'fields': ['dam_height',
                                       'dam_width',
                                       'spillway_elevation',
                                       'top_of_dam',
                                       'num_of_floodgates',
                                       'discharge_capacity']})
    ]

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
admin.site.register(StoryContent, StoryContentAdmin)
admin.site.register(LakeStatistics, LakeStatisticsAdmin)
