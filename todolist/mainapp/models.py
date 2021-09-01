from django.db import models

from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=None)
    users = models.ManyToManyField(CustomUser)


class ToDo(models.Model):
    text = models.TextField()
    part_of_project = models.ManyToOneRel(Project)
    created_by = models.ForeignKey(CustomUser)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

