from django.conf.urls import patterns, include, url
# from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()
from djangoproject import views
from django.shortcuts import HttpResponse
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap, Sitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post
from blog.views import projects
import settings
import datetime

post_index = {
    'queryset': Post.publics.all(),
    'date_field': 'created',
}


class AbstractSitemapClass():
    changefreq = 'daily'
    url = None

    def get_absolute_url(self):
        return self.url


class StaticSitemap(Sitemap):
    pages = {
        'home': '/',  # Add more static pages here like this 'example':'url_of_example',
        'rates': '/rates/',
    }
    main_sitemaps = []
    for page in pages.keys():
        sitemap_class = AbstractSitemapClass()
        sitemap_class.url = pages[page]
        main_sitemaps.append(sitemap_class)

    def items(self):
        return self.main_sitemaps

    lastmod = datetime.datetime(2014, 4, 1)  # Enter the year,month, date you want in yout static page sitemap.
    priority = 1
    changefreq = "yearly"

sitemaps = {
    'main': StaticSitemap,
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(post_index, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^rates/', include('rates.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.flat_page, name='about'),
    url(r'^projects/$', projects, name='projects'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /admin/", mimetype="text/plain")),
    # url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
        settings.MEDIA_ROOT}))
