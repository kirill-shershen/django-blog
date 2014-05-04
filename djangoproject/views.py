from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage


def flat_page(request):
    flatpage = FlatPage.objects.get(url=request.path)
    return render(request, 'flat_page.html', locals())
