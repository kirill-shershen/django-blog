from django.contrib import admin
from rates.models import Bank, BankContact
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    list_display = ('bank', 'contacttype', 'value')

admin.site.register(Bank, BankAdmin)
admin.site.register(BankContact, ContactAdmin)