from django.urls import path
from . import views

urlpatterns = [
    path('check_mfa', views.check_mfa, name='check_mfa'), # devrait pas apparaitre en url comme les login/sign success, comment faire?
    path('qrcode', views.qrcode_gen, name='qrcode'),
    path('signin', views.SignInUser, name="signin"),
    path('login', views.LoginUser, name="login"),
    path('', views.LoginUser, name="login"),

]