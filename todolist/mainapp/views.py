from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from mainapp.serializers import ProjectSerializer, ToDoSerializer
from .filters import ToDoFilter, ProjectFilter
from .models import Project, ToDo


class ResultsPaginationIsTen(PageNumberPagination):
    page_size = 10


class ResultsPaginationIsTwenty(PageNumberPagination):
    page_size = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ResultsPaginationIsTen
    filterset_class = ProjectFilter


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ResultsPaginationIsTwenty
    filterset_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):
        ToDo.objects.filter(pk=kwargs['pk']).save(is_active=False)
        return Response(status=status.HTTP_204_NO_CONTENT)
