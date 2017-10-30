"""
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
from django.conf.urls import url, include
from django.contrib.gis import admin
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from restapi import views
import django.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^household/', views.householddetail),
    url(r'^farm/', views.farmdetail),
    url(r'^crop/', views.cropdetail),
    url(r'^well/', views.welldetail),
    url(r'^member/', views.memberdetail),
    url(r'^season/', views.seasondetail),
    url(r'^storage/', views.storagedetail),
    url(r'^farmphoto/', views.farmphoto),
    url(r'^storagephoto/', views.storagephoto),
    url(r'^wellphoto/', views.wellphoto),
    url(r'^farmvideo/', views.farmvideo),
    url(r'^householdphoto/', views.householdphoto),
    url(r'^householdvideo/', views.householdvideo),
    url(r'^householdaudio/', views.householdaudio),
    url(r'^storagevideo/', views.storagevideo),
    url(r'^wellvideo/', views.wellvideo),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
