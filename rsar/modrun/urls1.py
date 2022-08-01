from django import views
from .import views
from django.conf import settings
from django.urls import path

urlpatterns = [
    path("", views.home, name = "home"),
    path('home', views.home, name="home")

]
