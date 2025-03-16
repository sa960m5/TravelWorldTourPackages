from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    vendors = models.CharField(max_length=255, blank=True, null=True)  # Add this line

    def __str__(self):
        return self.username