from django.urls import path
from . import views

urlpatterns = [
    path('mfa-check', views.mfa_check, name='mfa-check'),
    
    path('qrcode-check', views.qrcode_check, name="qrcode-check"),
    path('enable-mfa-qrcode', views.enable_mfa_qrcode, name='enable-mfa-qrcode'),
    
    path('login', views.LoginUser, name="login"),
    path('logout', views.LogOutUser, name="logout"),
    
    path('signin', views.SignInUser, name="signin"),
    
    path('', views.LoginUser, name="login"),
]