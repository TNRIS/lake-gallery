from django.conf.urls import url

from . import views


app_name = 'map'
urlpatterns = [
    url(r'^([A-P]{1})/$', views.index, name='region'),
    url(r'^([a-p]{1})/$', views.redirect_region),
    url(r'^$', views.index, name='index')
]
