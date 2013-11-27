from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Post

def index(request):
	return render(request, 'index.html')

def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "tagpage.html", locals())
