#coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-created'), template_name='blog.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='post_detail.html')),
    url(r'^archives/$', ListView.as_view(queryset=Post.objects.all().order_by('-created'), template_name='archives.html')),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
)