from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=10)


class Category(models.Model):
    name = models.CharField(max_length=10)


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_time = models.DateTimeField(auto_created=True)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Tag, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


