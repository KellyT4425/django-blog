from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import About
# Create your views here.


def about_details(request):
    about = About.objects.all().order_by('-updated_on').first()
    # possible error.

    return render(
        request,
        'about_me/about.html',
        {"about": about},
    )
