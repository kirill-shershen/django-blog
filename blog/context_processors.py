# -*- coding: utf-8 -*-
from blog.models import Post
from calendar import month_name, monthrange
import time 
import datetime
from django.db.models.functions import TruncMonth
from django.db.models import Count

def get_month_list(request):
    if not Post.publics.count():
        return []

    months = Post.objects.filter(public=True).annotate(month=TruncMonth('created')).values('month').annotate(c=Count('id'))[:12]

    return {'month_list': months}