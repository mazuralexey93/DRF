from django.db import models

from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f' {self.name}'


class ToDo(models.Model):
    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
