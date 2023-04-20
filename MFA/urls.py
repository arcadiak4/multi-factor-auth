from django.urls import path
from . import views

urlpatterns = [
    path('check_mfa', views.check_mfa, name='check_mfa'),
    path('qrcode', views.qrcode_gen, name='qrcode'),
    
    path('login', views.LoginUser, name="login"),
    path('logout', views.LogOutUser, name="logout"),
    
    path('signin', views.SignInUser, name="signin"),
    
    path('', views.LoginUser, name="login"),

]