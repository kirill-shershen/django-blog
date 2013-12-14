from django.contrib import admin
from blog.models import Post
# Register your models here.
from tinymce.widgets import TinyMCE
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse
from djangoproject import settings

class CollectionAdmin(admin.ModelAdmin):
 
    class Media:
        js = (
            '%stinymce/tiny_mce.js' % settings.STATIC_URL, 
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce_src.js',
            '%stinymce/tiny_mce_init.js' % settings.STATIC_URL,
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        )

admin.site.register(Post, CollectionAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CollectionAdmin)
