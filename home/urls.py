from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home_view,name="home"),
    path('contact/',contact_view,name="contact"),
    path('about/', about_view , name="about"),
    path('categories/', categories_view , name="categories"),
    #path('post-<int:pid>', categories_view , name="single"),

]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)