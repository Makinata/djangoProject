from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:req>', views.HttpResponse),
]