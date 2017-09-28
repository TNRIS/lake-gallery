from django.contrib.gis import admin
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks, StoryContent


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')


class StoryContentAdmin(admin.ModelAdmin):
    list_display = ['lake']

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
admin.site.register(StoryContent, StoryContentAdmin)
