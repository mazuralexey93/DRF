from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from mainapp.serializers import ProjectSerializer, ToDoSerializer
from .filters import ToDoFilter
from .models import Project, ToDo


class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoAPIView(APIView):
    def get(self, request, format=None):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)


class ToDoCreateAPIView(CreateAPIView):
    """
    !!! NOT NULL constraint failed: mainapp_todo.project_id
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoListAPIView(ListAPIView):
    # renderer_classes = [JSONRenderer]
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


class ToDoQuerySetFilterViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):
        """http://127.0.0.1:8000/views/set/filtering/?text=done"""
        qs = super().get_queryset()
        text_contains = self.request.query_params.get('text', '')
        return qs.filter(text__contains=text_contains)


class ToDoKwargsFilterView(ListAPIView):
    """http://127.0.0.1:8000/views/todo/important/"""
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        text_contains = self.kwargs.get('text', '')
        return qs.filter(text__contains=text_contains)


class ArticleDjangoFilterViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/djangofiltering/?text=sdsdssax"""
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filterset_fields = ['text', 'user']


class ArticleCustomDjangoFilterViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/customfilter/?text=important%20todo!"""
    renderer_classes = [JSONRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filterset_class = ToDoFilter


class LimitOffsetPaginationByTwo(LimitOffsetPagination):
    default_limit = 2


class ArticleLimitOffsetPaginatonViewSet(ModelViewSet):
    """http://127.0.0.1:8000/views/set/pagination/"""
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = LimitOffsetPaginationByTwo
