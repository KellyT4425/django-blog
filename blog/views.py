from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    # queryset = Post.objects.filter(author=2)  # filtering by author.
    # queryset = Post.objects.all().order_by("created_on") -created_on orders in reverse.
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        # The object assigning the above post variable to post to allow post.content, post.author in template.
        {"post": post},

    )
