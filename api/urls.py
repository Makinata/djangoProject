from django.urls import path
from . import views

urlpatterns = [
    path('<str:req>', views.Query_broker_View.as_view()),
]