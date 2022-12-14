from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import ContactForm

# Create your views here.


def home_view(request,cat_name=None):
    posts = Post.objects.filter(promote=1)
    if cat_name != None:
        posts = posts.filter(category__title=cat_name)
    posts = Paginator(posts,4)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {
        "posts":posts
    }
    return render(request,"index.html",context)

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()    
    return render(request,"page-contact.html",{"form":form})

def about_view(request):
    return render(request,"page-about.html")


def categories_view(request):
    categories = Category.objects.all()
    categories = Paginator(categories,8)
    page_number = request.GET.get('page')
    categories = categories.get_page(page_number)

    return render(request,"category.html",{"categories":categories})


def single_view(request,pid):
    posts=Post.objects.filter(promote=True)
    post = get_object_or_404(posts,pk=pid)
    context ={
        "post":post
    }
    return render(request,"single-standard.html",context)
