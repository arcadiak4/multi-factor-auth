from django.db import models

from django.utils.translation import gettext as _


class CustomUser(models.Model):
    username = models.CharField(
        max_length=100,
        default="",
        verbose_name=_("Username"),
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=100,
        verbose_name=_("Password"),
        default="",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.username}"
