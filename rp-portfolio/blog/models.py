from django.db import models
from django.forms import ModelForm

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('r', 'Review'),
    ('t', 'Trash'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title
