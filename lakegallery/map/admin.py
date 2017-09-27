from django.contrib.gis import admin
from .models import MajorReservoirs, RWPAs, HistoricalAerialLinks

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
admin.site.register(HistoricalAerialLinks)
