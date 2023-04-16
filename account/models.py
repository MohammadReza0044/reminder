from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    is_manager = models.BooleanField(default=False)
    is_modire_ejraei = models.BooleanField(default=False)
