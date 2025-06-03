from django.db import models
from django.contrib.auth.models import User

# CONSTANTS
"""
two tuples - first values 0, 1 are stored in the database.
the second values, Draft and Published are displayed as the option
in the select form input.
"""
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    # generates a single-line form input type text (string).
    title = models.CharField(max_length=200, unique=True)
    # generates a single-line form input text (string), short label.
    slug = models.SlugField(max_length=200, unique=True)
    # generates a select drop down menu populated by user data (string).
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    # generates a multi-line teatarea input (string).
    content = models.TextField()
    # auto_now_add=True this generates the computers time when post saved.
    created_on = models.DateTimeField(auto_now_add=True)
    # using the above STATUS constant to re-assign 0, 1 to Draft and Published.
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
