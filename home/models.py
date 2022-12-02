from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/" , null=False, blank=False)
    description= models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", null=False, blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    promote = models.BooleanField(default=False)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField(upload_to="category/", null=False, blank=False)
