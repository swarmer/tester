from django.conf.urls import patterns, include, url
from django.contrib import admin

from allauth.account import views as allauth_views

from . import views


urlpatterns = [
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # django-allauth
    url(r'^accounts/signup/$', allauth_views.signup, name='account_signup'),
    url(r'^accounts/login/$', allauth_views.login, name='account_login'),
    url(r'^accounts/logout/$', allauth_views.logout, name='account_logout'),
    url(r'^accounts/inactive/$', allauth_views.account_inactive,
        name='account_inactive'),

    # core
    url(r'^$', views.index, name='index'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^test/([\w-]+)/([\w-]+)/$', views.test, name='test'),

    # AJAX
    url(r'^miniapi/questions/save_active/$', views.save_active_questions),
]
