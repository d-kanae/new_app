from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("user-register", views.user_register, name="user-register"),
    path("search", views.index, name="search"),
    path("register", views.index, name="register"),
]
