from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):


    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        USER = "USER", "User"


    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']