from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, delete all associated posts
    created_date = models.DateTimeField(auto_now_add=True) # Set field to current time when post is added
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True) # null means unpublished 

    def __str__(self):
        return self.title