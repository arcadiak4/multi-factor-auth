from django.http import HttpResponse

from django.views.generic.edit import FormView

from django.template.loader import render_to_string

from .forms import (
    LoginForm,
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

        return HttpResponse(
            render_to_string(
                "multifactor/login_success.html", {"username": form.cleaned_data['username']}
            )
        )
