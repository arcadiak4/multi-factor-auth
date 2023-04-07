from django.urls import path

from . import views

urlpatterns = [
    path('signin', views.SignInUser.as_view(), name="signin"),
    path('', views.LoginUser.as_view(), name="login"),
]