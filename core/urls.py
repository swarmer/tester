from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from allauth.account import views as allauth_views

from . import views


urlpatterns = [
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # django-allauth
    url(
        r'^accounts/signup/$',
        RedirectView.as_view(pattern_name='account_login'),
        name='account_signup'
    ),
    url(r'^accounts/login/$', allauth_views.login, name='account_login'),
    url(r'^accounts/logout/$', allauth_views.logout, name='account_logout'),
    url(r'^accounts/inactive/$', allauth_views.account_inactive,
        name='account_inactive'),

    url(r'^accounts/social/', include('allauth.socialaccount.urls')),
    url(r'^accounts/', include('allauth.socialaccount.providers.vk.urls')),

    # core
    url(r'^$', views.index, name='index'),
    url(r'^explore/$', views.explore, name='explore'),

    url(r'^test/new/$', views.test_new, name='test_new'),
    url(r'^test/([\w-]+)/([\w-]+)/$', views.test, name='test'),
    url(r'^test/([\w-]+)/([\w-]+)/edit/$', views.test_edit, name='test_edit'),
    url(r'^test/([\w-]+)/([\w-]+)/delete/$', views.test_delete, name='test_delete'),

    # AJAX
    url(r'^miniapi/questions/save_active/$', views.save_active_questions),
]
