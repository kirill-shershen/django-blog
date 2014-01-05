from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Post
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
    paginate_by=10

def month(request, year, month):
    """Monthly archive."""
    object_list = Post.publics.filter(created__range = (datetime.date(int(year),int(month),1),datetime.date(int(year),int(month),monthrange(int(year), int(month))[1])))
    return render(request, "archives.html", locals())