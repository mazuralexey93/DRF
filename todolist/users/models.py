from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f' {self.first_name}, {self.last_name}'


class CustomUserRole(models.Model):
    role = models.CharField(max_length=128)
    user = models.OneToOneField(CustomUser)

    def __str__(self):
        return f'{self.role}'
