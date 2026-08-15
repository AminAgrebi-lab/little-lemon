# App-level URL configuration
from django.urls import path
from . import views

urlpatterns = [
    # The template references this route via {% url 'home' %}
    path('', views.index, name='home'),
]
