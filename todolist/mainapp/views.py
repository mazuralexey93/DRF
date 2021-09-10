from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from mainapp.serializers import ProjectSerializer, ToDoSerializer
from .filters import ToDoFilter, ProjectFilter
from .models import Project, ToDo


class ToDoAPIView(APIView):
    def get(self, request, format=None):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ProjectAPIView(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ToDoCreateAPIView(CreateAPIView):
    """
    !!! NOT NULL constraint failed: mainapp_todo.project_id
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProjectCreateAPIView(CreateAPIView):
    """!!!"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoListAPIView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoDeleteAPIView(DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProjectDeleteAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoUpdateAPIView(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ProjectUpdateAPIView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ViewSet):
    def list(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def is_active(self, request, pk=None):
        todo = get_object_or_404(ToDo, pk=pk)
        return Response({'todo.is_active': todo.is_active})


class ProjectViewSet(ViewSet):
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_object_or_404(ToDo, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ToDoQuerySetFilterViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):
        """http://127.0.0.1:8000/views/set/filtering/?text=done"""
        qs = super().get_queryset()
        text_contains = self.request.query_params.get('text', '')
        return qs.filter(text__contains=text_contains)

#
# class ToDoKwargsFilterView(ListAPIView):
#     """http://127.0.0.1:8000/views/todo/important/"""
#     serializer_class = ToDoSerializer
#     queryset = ToDo.objects.all()
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         text_contains = self.kwargs.get('text', '')
#         return qs.filter(text__contains=text_contains)

#
# class ToDoDjangoFilterViewSet(ModelViewSet):
#     """http://127.0.0.1:8000/views/set/djangofiltering/?text=sdsdssax"""
#     renderer_classes = [JSONRenderer]
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer
#     filterset_fields = ['text', 'user']


class ToDoCustomDjangoFilterViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/customtodofilter/?text=important%20todo!"""
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filterset_class = ToDoFilter


class ProjectCustomDjangoFilterViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/customprojectfilter/?name=project2"""
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter


class LimitOffsetPaginationByTwo(LimitOffsetPagination):
    default_limit = 2


class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/pagination/"""
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = LimitOffsetPaginationByTwo
