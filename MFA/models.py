from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext as _

class User(AbstractUser):
    first_name = models.CharField(
        max_length=100,
        default="",
        verbose_name=_("First Name"),
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=100,
        default="",
        verbose_name=_("Last Name"),
        null=False,
        blank=False
    )

    username = models.CharField(
        unique=True,
        max_length=100,
        default="",
        verbose_name=_("Username"),
        null=False,
        blank=False
    )

    mfa_key = models.CharField(
        max_length=100,
        default="",
        null=False,
        blank=False,
    )