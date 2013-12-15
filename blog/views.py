from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Post
from django.views.generic import ListView

def index(request):
	return render(request, 'index.html')

def tagpage(request, tag):
    posts = Post.public.filter(tags__name=tag)
    return render(request, "tagpage.html", locals())

class PostListView(ListView):
    """docstring for PostListView"""
    model = Post
    paginate_by=10

        