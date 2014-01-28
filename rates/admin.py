from django.contrib import admin
from rates.models import Bank, BankContacts
# Register your models here.

class BankAdmin(admin.ModelAdmin):
    ordering = ('name')

admin.site.register(Bank, BankAdmin)
admin.site.register(BankContacts)