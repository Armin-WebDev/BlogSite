from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.


def home_view(request):
    posts = Post.objects.filter(promote=True)
    context = {
        "posts":posts
    }
    return render(request,"index.html",context)

def contact_view(request):
    return render(request,"page-contact.html")

def about_view(request):
    return render(request,"page-about.html")


def categories_view(request):
    return render(request,"category.html")


def single_view(request,pid):
    posts=Post.objects.filter(promote=True)
    post = get_object_or_404(posts,pk=pid)
    context ={
        "post":post
    }
    return render(request,"single-standard.html",context)
