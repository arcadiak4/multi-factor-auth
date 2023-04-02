from django import forms
from .models import CustomUser

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
