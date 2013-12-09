from django.conf.urls import patterns, include, url
# from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()
import settings
from djangoproject import views 

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.flat_page, name='about'),
    url(r'^projects/$', views.flat_page, name='projects'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^admin/filebrowser/', include(site.urls)),
)