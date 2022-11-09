from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:a>/<int:b>', views.index),
]