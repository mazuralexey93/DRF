from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import ProjectSerializer,ToDoSerializer
from .models import Project, ToDo


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoAPIView(APIView):
    # renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


"""
!!! NOT NULL constraint failed: mainapp_todo.project_id
"""


class ToDoCreateAPIView(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDeleteAPIView(DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoUpdateAPIView(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
