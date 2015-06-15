from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


urlpatterns = patterns('core.views',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index),
    url(r'^explore', views.explore),
)
