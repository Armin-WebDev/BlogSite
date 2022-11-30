from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home_view,name="home"),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)