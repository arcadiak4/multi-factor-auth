from django.urls import path
from . import views

urlpatterns = [
    path('check-mfa', views.check_mfa, name='check-mfa'),
    path('qrcode', views.qrcode_gen, name='qrcode'),
    path('qrcode-check', views.qrcode_check, name="qrcode-check"),
    
    path('login', views.LoginUser, name="login"),
    path('logout', views.LogOutUser, name="logout"),
    
    path('signin', views.SignInUser, name="signin"),
    
    path('', views.LoginUser, name="login"),
]