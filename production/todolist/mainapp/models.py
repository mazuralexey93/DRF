from django.db import models

from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(CustomUser)


    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f' {self.name}'


class ToDo(models.Model):

    class ToDoStatusChoices(models.TextChoices):
        ACTIVE = 'ACT', 'Активно'
        CLOSED = 'CLS', 'Закрыто'

    text = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=3,
                              choices=ToDoStatusChoices.choices,
                              default=ToDoStatusChoices.ACTIVE)

    class Meta:
        ordering = ['pk']
