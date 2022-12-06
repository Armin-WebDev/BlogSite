from django.shortcuts import render
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