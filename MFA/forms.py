from django import forms
from .models import CustomUser

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
