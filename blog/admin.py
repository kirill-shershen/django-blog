from django.contrib import admin
from blog.models import Post
# Register your models here.
from tinymce.widgets import TinyMCE
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

class CollectionAdmin(admin.ModelAdmin):
 
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce_src.js', 
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce_src.js',
            '/static/tiny_mce/tiny_mce.js',
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        )

admin.site.register(Post, CollectionAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
