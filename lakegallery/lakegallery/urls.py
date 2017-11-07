"""lakegallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import (include, url, handler400, handler403,
                              handler404, handler500)
from django.contrib.gis import admin
from django.conf import settings
from api.api import router

handler400 = 'map.views.bad_request'
handler403 = 'map.views.permission_denied'
handler404 = 'map.views.page_not_found'
handler500 = 'map.views.server_error'

urlpatterns = [
    url(r'^', include('map.urls')),
    url(r'^api/', include(router.urls)),
    # disabled browsable api authentication since nothing is editable
    # url(r'^api-auth/', include('rest_framework.urls',
    #     namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
