from django.contrib.gis import admin
from .models import (MajorReservoirs, RWPAs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics, SignificantEvents,
                     BoatRamps, ChannelMarkers, Hazards, Parks)


class MajorReservoirsAdmin(admin.OSMGeoAdmin):
    list_display = ['res_lbl', 'region', 'story']
    ordering = ['region', 'res_lbl']
    list_filter = ['region']


class RWPAsAdmin(admin.OSMGeoAdmin):
    list_display = ['letter', 'reg_name']
    ordering = ['letter']


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')
    ordering = ('lake', 'year', 'link')
    list_per_page = 50
    list_filter = ['lake']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(HistoricalAerialLinksAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class StoryContentAdmin(admin.ModelAdmin):
    list_display = ['lake']
    ordering = ['lake']
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(StoryContentAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class LakeStatisticsAdmin(admin.ModelAdmin):
    list_display = ['lake']
    ordering = ['lake']
    fieldsets = [
        (None, {'fields': ['lake', 'wdft_link']}),
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(LakeStatisticsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class SignificantEventsAdmin(admin.ModelAdmin):
    list_display = ('lake', 'event_type', 'date', 'height')
    ordering = ('lake', 'event_type', 'date')
    list_per_page = 50
    list_filter = ['lake', 'event_type']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(SignificantEventsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


"""
Overlay Layers for stories (points of interest)
"""


class BoatRampsAdmin(admin.ModelAdmin):
    list_display = ('lake', 'name')
    ordering = ('lake', 'name')
    list_per_page = 50
    list_filter = ['lake']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(BoatRampsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class ChannelMarkersAdmin(admin.ModelAdmin):
    list_display = ('lake', 'marker_id')
    ordering = ('lake', 'marker_id')
    list_per_page = 50
    list_filter = ['lake']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(ChannelMarkersAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class HazardsAdmin(admin.ModelAdmin):
    list_display = ('lake', 'hazard_type', 'num_buoys')
    ordering = ('lake', 'hazard_type')
    list_per_page = 50
    list_filter = ['lake']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(HazardsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class ParksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'name', 'park_type')
    ordering = ('lake', 'name')
    list_per_page = 50
    list_filter = ['lake']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(ParksAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


admin.site.register(MajorReservoirs, MajorReservoirsAdmin)
admin.site.register(RWPAs, RWPAsAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
admin.site.register(StoryContent, StoryContentAdmin)
admin.site.register(LakeStatistics, LakeStatisticsAdmin)
admin.site.register(SignificantEvents, SignificantEventsAdmin)
admin.site.register(BoatRamps, BoatRampsAdmin)
admin.site.register(ChannelMarkers, ChannelMarkersAdmin)
admin.site.register(Hazards, HazardsAdmin)
admin.site.register(Parks, ParksAdmin)

admin.site.site_header = "Texas Lake Gallery - Administration"
admin.site.index_title = "Database Tables"
