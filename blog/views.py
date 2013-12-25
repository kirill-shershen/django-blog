from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Post
from django.views.generic import ListView


def index(request):
	return render(request, 'index.html')

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "tagpage.html", locals())

class PostListView(ListView):
    """docstring for PostListView"""
    model = Post
    paginate_by=10

def month(request, year, month):
    """Monthly archive."""
    posts = Post.publics.filter(created__year=year, created__month=month)
    return render_to_response("archives.html", dict(post_list=posts, user=request.user, archive=True))