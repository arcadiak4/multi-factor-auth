from django.urls import path

from . import views

urlpatterns = [
    path('qrcode', views.qrcode_gen, name='qrcode'),
    path('signin', views.SignInUser.as_view(), name="signin"),
    path('', views.LoginUser.as_view(), name="login"),
]