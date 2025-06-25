from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.about_details, name='about')

]
