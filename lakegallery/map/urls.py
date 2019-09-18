from django.conf.urls import url

from . import views
from django.views.generic.base import RedirectView

app_name = 'map'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^about', RedirectView.as_view(url='about/')),
    url(r'^([\w|\W]+)$', views.story, name='story')
]
