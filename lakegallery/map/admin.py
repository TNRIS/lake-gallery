from django.contrib.gis import admin
from .models import (MajorReservoirs, HistoricalAerialLinks,
                     StoryContent, LakeStatistics, SignificantEvents,
                     BoatRamps, ChannelMarkers, Hazards, Parks)


class MajorReservoirsAdmin(admin.OSMGeoAdmin):
    list_display = ['res_lbl', 'story']
    ordering = ['res_lbl']
    list_per_page = 50
    list_filter = ['story', 'type', 'status']
    search_fields = ['res_lbl']


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')
    ordering = ('lake', 'year', 'link')
    list_per_page = 50
    search_fields = ['lake__res_lbl', 'year'] # search related field

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
        ('Main "Story" Page', {'fields': ['lake', 'summary',
                                          ('summary_photo_main',
                                           'summ_main_tag')]}),
        ('History Page', {'fields': ['history',
                                     ('history_photo_main', 'hist_main_tag'),
                                     ('history_photo', 'hist_tag')]}),
        ('Additional Page 1', {'fields':
                               ['section_one_nav',
                                'section_one_header',
                                ('section_one_photo_main',
                                 'one_main_tag'),
                                'section_one_content',
                                ('section_one_photo', 'one_tag')]}),
        ('Additional Page 2', {'fields':
                               ['section_two_nav',
                                'section_two_header',
                                ('section_two_photo_main',
                                 'two_main_tag'),
                                'section_two_content',
                                ('section_two_photo', 'two_tag')]}),
        ('Additional Page 3', {'fields':
                               ['section_three_nav',
                                'section_three_header',
                                ('section_three_photo_main',
                                 'three_main_tag'),
                                'section_three_content',
                                ('section_three_photo',
                                 'three_tag')]}),
    ]
    readonly_fields = ('summ_main_tag', 'hist_main_tag', 'hist_tag',
                       'one_main_tag', 'one_tag', 'two_main_tag', 'two_tag',
                       'three_main_tag', 'three_tag')
    search_fields = ['lake__res_lbl'] # search related res_lbl field

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
    list_filter = ['primary_purposes', 'location']
    search_fields = ['lake__res_lbl'] # search related res_lbl field & location

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
    list_filter = ['event_type']
    search_fields = ['lake__res_lbl'] # search related res_lbl field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(SignificantEventsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


"""
Overlay Layers for stories (points of interest)
"""


class BoatRampsAdmin(admin.OSMGeoAdmin):
    list_display = ('lake', 'name', 'operator')
    ordering = ('lake', 'name', 'operator')
    list_per_page = 50
    list_filter = ['operator']
    search_fields = ['lake__res_lbl', 'name'] # search related res_lbl field, name & operator

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(BoatRampsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class ChannelMarkersAdmin(admin.OSMGeoAdmin):
    list_display = ('lake', 'marker_id', 'year')
    ordering = ('lake', 'marker_id', 'year')
    list_per_page = 50
    list_filter = ['year']
    search_fields = ['lake__res_lbl'] # search related res_lbl field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(ChannelMarkersAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class HazardsAdmin(admin.OSMGeoAdmin):
    list_display = ('lake', 'hazard_type', 'num_buoys')
    ordering = ('lake', 'hazard_type')
    list_per_page = 50
    list_filter = ['hazard_type']
    search_fields = ['lake__res_lbl'] # search related res_lbl field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(HazardsAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


class ParksAdmin(admin.OSMGeoAdmin):
    list_display = ('lake', 'name', 'park_type')
    ordering = ('lake', 'name')
    list_per_page = 50
    list_filter = ['park_type']
    search_fields = ['lake__res_lbl'] # search related res_lbl field

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "lake":
            kwargs["queryset"] = (MajorReservoirs.objects.all()
                                  .order_by('res_lbl'))
        return (super(ParksAdmin, self)
                .formfield_for_foreignkey(db_field, request, **kwargs))


admin.site.register(MajorReservoirs, MajorReservoirsAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
admin.site.register(StoryContent, StoryContentAdmin)
admin.site.register(LakeStatistics, LakeStatisticsAdmin)
admin.site.register(SignificantEvents, SignificantEventsAdmin)
admin.site.register(BoatRamps, BoatRampsAdmin)
admin.site.register(ChannelMarkers, ChannelMarkersAdmin)
admin.site.register(Hazards, HazardsAdmin)
admin.site.register(Parks, ParksAdmin)

admin.site.index_title = "Database Tables"
