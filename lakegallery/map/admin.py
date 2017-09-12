from django.contrib.gis import admin
from .models import MajorReservoirs, RWPAs

admin.site.register(MajorReservoirs, admin.OSMGeoAdmin)
admin.site.register(RWPAs, admin.OSMGeoAdmin)
