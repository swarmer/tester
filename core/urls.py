from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = patterns('core.views',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^logout', auth_views.logout, {'next_page': '/'}),
    url(r'^login', auth_views.login),

    url(r'^$', views.index),
    url(r'^explore/$', views.explore),
    url(r'test/([\w-]+)/([\w-]+)/$', views.test),
)
