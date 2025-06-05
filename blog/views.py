from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    # queryset = Post.objects.filter(author=2)  # filtering by author.
    # queryset = Post.objects.all().order_by("created_on") -created_on orders in reverse.
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
