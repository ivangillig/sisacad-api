from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractUser):

    """User model."""

    username = None
    email = models.EmailField(('Email institucional'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #asked in console

    objects = UserManager()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email