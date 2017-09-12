from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from map.models import MajorReservoirs, RWPAs

from . import views

app_name = 'map'
urlpatterns = [
    url(r'^majorres.geojson$',
        GeoJSONLayerView.as_view(model=MajorReservoirs), name='majorres'),
    url(r'^rwpas.geojson$',
        GeoJSONLayerView.as_view(model=RWPAs), name='rwpas'),
    url(r'^$', views.index, name='index')
]
