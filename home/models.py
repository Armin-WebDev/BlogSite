from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/" , null=False, blank=False)
    description= models.TextField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Post(models.Model):
    title = models.CharField(max_length=127)
    content = RichTextField()
    image = models.ImageField(upload_to="blog/", null=False, blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    promote = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    image=models.ImageField(upload_to="category/", null=False, blank=False)

    def __str__(self) -> str:
        return self.title
