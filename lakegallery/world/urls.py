from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from world.models import WorldBorder

from . import views

app_name = 'world'
urlpatterns = [
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='mpoly'), name='data'),
    url(r'^$', views.index, name='index')
]
