from django.conf.urls import url

from djgeojson.views import GeoJSONLayerView

from world.models import WorldBorder

from . import views

app_name = 'world'
urlpatterns = [
    # ex: /world/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
