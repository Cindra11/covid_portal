"""covid_portal URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('beds/', include('beds.urls')),
    path('admin/', admin.site.urls),
]
