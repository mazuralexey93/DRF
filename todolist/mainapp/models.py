from django.db import models

from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=1024)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f' {self.name}'


class ToDo(models.Model):
    name = models.CharField(max_length=128, default='Another ToDo note')
    text = models.TextField()
    part_of_project = models.ManyToOneRel(Project)
    created_by = models.ForeignKey(CustomUser, models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

