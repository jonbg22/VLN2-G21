from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # http://localhost:8000/myProfile
    path('', views.index, name="index"),
]