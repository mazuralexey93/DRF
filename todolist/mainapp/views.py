from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import ProjectSerializer
from .models import Project


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
