from django.urls import path

from . import views

urlpatterns = [
    path('',views.blog, name ="blog"),
    path('add',views.add, name = "add"),
]