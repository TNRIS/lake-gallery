from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from map.models import MajorReservoirs, RWPAs

from . import views


class MapLayer(GeoJSONLayerView):
    # Options
    # precision = 4   # float
    simplify = 0.9  # generalization
    geometry_field = 'geom'

app_name = 'map'
urlpatterns = [
    url(r'^majorres.geojson$',
        MapLayer.as_view(model=MajorReservoirs,
                         properties=('res_lbl', 'region')), name='majorres'),
    url(r'^rwpas.geojson$',
        MapLayer.as_view(model=RWPAs,
                         properties=('reg_name', 'letter')), name='rwpas'),
    url(r'^([A-P]{1})/$', views.index, name='region'),
    url(r'^$', views.index, name='index')
]
