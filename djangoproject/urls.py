from django.conf.urls import patterns, include, url
# from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()
import settings
from djangoproject import views 
from django.shortcuts import HttpResponse
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post

post_index = {
             'queryset': Post.publics.all(),
             'date_field': 'created',
}

sitemaps = {
            'flatpages': FlatPageSitemap,
            'blog': GenericSitemap(post_index, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^rates/', include('rates.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.flat_page, name='about'),
    url(r'^projects/$', views.flat_page, name='projects'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/", mimetype="text/plain")),
    # url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
)