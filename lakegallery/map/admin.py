from django.contrib.gis import admin
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks


class HistoricalAerialLinksAdmin(admin.ModelAdmin):
    list_display = ('lake', 'year', 'link')

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
admin.site.register(HistoricalAerialLinks, HistoricalAerialLinksAdmin)
