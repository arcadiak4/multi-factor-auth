from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from .models import CustomUser

class SignInForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "password1", "password2")

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )

'''
class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "password")

    first_name = forms.CharField(
        required=True
    )

    last_name = forms.CharField(
        required=True
    )

    username = forms.CharField(
        required=True
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput()
    )
'''

'''
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")

    username = forms.CharField(
        required=True
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput()
    )
'''