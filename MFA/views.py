from django.http import HttpResponse

from django.views.generic.edit import (
    CreateView,
    FormView,
)

from django.template.loader import render_to_string

from .models import CustomUser

from .forms import (
    LoginForm,
    SigninForm,
)

import base64
import hashlib
import secrets

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    hash = hashlib.pbkdf2_hmac(
        'sha3-256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000,
    )
    
    b64_hash = base64.b64encode(hash).decode("ascii").strip()

    return b64_hash, salt

class SignInUser(CreateView):
    """FormView to sign in
    All form fields of CustomUser are sent to signin.html
    """

    template_name = "multifactor/signin.html"
    form_class = SigninForm

    def form_valid(self, form):
        """Goes to signin_success.html
        Returns user
        """

        form.instance.hash, form.instance.salt = hash_password(form.cleaned_data['password'])
        form.save()

        return HttpResponse(
            render_to_string(
                "multifactor/signin_success.html", {"username": form.cleaned_data['username']}
            )
        )


class LoginUser(FormView):
    """FormView to log in
    All form fields of CustomUser are sent to login.html
    """

    template_name = "multifactor/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        """Goes to login_success.html
        Returns user
        """

        user = CustomUser.objects.filter(username=form.instance.username).first()

        if user is not None:
            good_password_hash = user.hash
            salt = user.salt

            hash_to_test = hash_password(form.cleaned_data['password'], salt)[0]
            
            if secrets.compare_digest(good_password_hash, hash_to_test):
                return HttpResponse(
                    render_to_string(
                        "multifactor/login_success.html", {"username": form.cleaned_data['username']}
                    )
                )
        
        form.add_error("username", 'Wrong username and/or password')
        return super().form_invalid(form)
