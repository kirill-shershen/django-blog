from django.shortcuts import render
from rates.models import Bank, BankContact, BankRate
from cbrcurrency import GetCurrentCurrency
# Create your views here.
def LastRates(request):
    last_time = BankRate.objects.order_by("-checktime")[0]
    banks = Bank.objects.all()
    bankcontacts = BankContact.objects.all()
    current_currency = GetCurrentCurrency()
    rates = BankRate.objects.filter(checktime=last_time.checktime).order_by('-value')
    return render(request, "rates.html", locals())