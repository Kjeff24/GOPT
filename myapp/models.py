from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    # log in with email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email