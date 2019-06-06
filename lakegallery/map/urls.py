from django.conf.urls import url

from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^([\w|\W]+)$', views.story, name='story')
]
