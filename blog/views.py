#coding: utf-8
from django.shortcuts import render
from blog.models import Post, Project
from django.views.generic import ListView
import datetime
from calendar import monthrange


def index(request):
    return render(request, 'index.html')


def tagpage(request, tag):
    object_list = Post.publics.filter(tags__name=tag)
    return render(request, "tagpage.html", locals())


class PostListView(ListView):
    """docstring for PostListView"""
    model = Post
    paginate_by = 10


def month(request, year, month):
    """Monthly archive."""
    object_list = Post.publics.filter(created__range=(datetime.date(int(year), int(month), 1), datetime.date(int(year), int(month), monthrange(int(year), int(month))[1])))
    return render(request, "archives.html", locals())


def projects(request):
    projects = Project.objects.all()
    # делаем плитку из массива кортежей по 5 записей
    kort = []
    i = 1
    recs = []
    for rec in projects:
        if i % 5 == 0:
            recs.append(rec)
            kort.append(tuple(recs))
            recs = []
        else:
            recs.append(rec)
            if i == len(projects):
                kort.append(tuple(recs))
        i += 1

    return render(request, 'project_list.html', locals())
