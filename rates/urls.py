#coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('rates.views',
    url(r'^$', "LastRates"),
)