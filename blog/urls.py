#coding: utf-8
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog.views import PostListView, month, tagpage

app_name = 'blog'
urlpatterns = [
    url(r'^$', PostListView.as_view(queryset=Post.publics.all(), template_name='blog.html')),
    url(r'^blog/page(?P<page>\d+)/$', PostListView.as_view(queryset=Post.publics.all(), template_name='blog.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='post_detail.html')),
    url(r'^archives/$', ListView.as_view(queryset=Post.publics.all(), template_name='archives.html')),
    url(r"^archives/(\d+)/(\d+)/$", month),
    url(r'^tag/(?P<tag>\w+)$', tagpage),
    # url(r'^projects/$', projects, name='projects'),
]