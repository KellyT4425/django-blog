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

    class Meta:
        """
        the - prefix puts items in descending order (3, 2, 1) newest to oldest,
        take it away and the order ascends instead (1, 2, 3) oldest to newest.
        if ? is prefixed then the list is randomised.
        """
        ordering = ["-created_on", "author"]

    def __str__(self):
        """
        When adding posts up till now, they have appeared in the admin panel as Post object(n),
        where n is an integer denoting the order of posts being added. Now, as per the main image,
        they are identified in a human-readable manner.
        The __str__() method has changed this post identifier to a string literal.
        By passing self as an argument to the __str__() method, you can use the field values in the f-string.
        """
        return f"The title of this post is {self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
