from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request,"index.html")

def contact_view(request):
    return render(request,"page-contact.html")

def about_view(request):
    return render(request,"page-about.html")