from django.conf.urls import url

from . import views

app_name = 'map'
urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^([\w|\W]+)$', views.story, name='story'),
    url(r'^([\w|\W]+)$', views.redirect_story),
    # 
    url(r'^$', views.index, name='index')
]
