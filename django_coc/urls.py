# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from coc.views.dispatcher import dispatch

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', dispatch, name='views.dispatcher'),
    url(r'^(?P<url>[\w|\W]+)', dispatch, name='views.dispatcher'),
    # Examples:
    # url(r'^$', 'django_coc.views.home', name='home'),
    # url(r'^django_coc/', include('django_coc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
