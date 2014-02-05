from django.shortcuts import render
from rates.models import Bank, BankContact, BankRate
# Create your views here.
def LastRates(request):
    last_time = BankRate.objects.order_by("-checktime")[0]
    banks = Bank.objects.all()
    bankcontacts = BankContact.objects.all()
    rates = BankRate.objects.filter(checktime=last_time.checktime)
    return render(request, "rates.html", locals())