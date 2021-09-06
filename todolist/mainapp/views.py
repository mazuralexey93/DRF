from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import ProjectSerializer,ToDoSerializer
from .models import Project, ToDo


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
