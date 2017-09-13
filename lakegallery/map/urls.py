from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from map.models import MajorReservoirs, RWPAs

from . import views


class MapLayer(GeoJSONLayerView):
    # Options
    # precision = 4   # float
    # simplify = 0.1  # generalization
    geometry_field = 'geom'
    properties = ('reg_name', 'letter')

app_name = 'map'
urlpatterns = [
    url(r'^majorres.geojson$',
        MapLayer.as_view(model=MajorReservoirs), name='majorres'),
    url(r'^rwpas.geojson$',
        MapLayer.as_view(model=RWPAs), name='rwpas'),
    url(r'^$', views.index, name='index')
]
