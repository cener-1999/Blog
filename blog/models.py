from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import re


class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(verbose_name="摘要",max_length=200,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.modified_time = timezone.now()

        if self.excerpt == '':
            self.excerpt = re.sub('([^\u4e00-\u9fa5\u0030-\u0039\s])','',self.body[:54])
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("blog:post",kwargs={"pk":self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)