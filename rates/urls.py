#coding: utf-8
from django.conf.urls import url
from rates.views import LastRates
urlpatterns = [
    url(r'^$', LastRates),
]