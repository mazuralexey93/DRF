from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import ProjectSerializer, ToDoSerializer
from .filters import ToDoFilter, ProjectFilter
from .models import Project, ToDo


class ProjectPaginator(PageNumberPagination):
    page_size = 10


class ToDoPaginator(PageNumberPagination):
    page_size = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # pagination_class = ProjectPaginator
    filterset_class = ProjectFilter
    # renderer_classes = JSONRenderer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # pagination_class = ToDoPaginator
    filterset_class = ToDoFilter


    # renderer_classes = JSONRenderer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
