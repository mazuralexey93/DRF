from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

import mainapp.views as mainapp

mainapp_router = DefaultRouter()

mainapp_router.register('todos', mainapp.ToDoViewSet,
                        basename='todo')  # /views/set/todos
mainapp_router.register('projects', mainapp.ProjectViewSet,
                        basename='project')  # /views/set/projects
# mainapp_router.register('filtering', mainapp.ToDoQuerySetFilterViewSet,
#                         basename='filter')  # /views/set/filtering
# mainapp_router.register('djangofiltering', mainapp.ToDoDjangoFilterViewSet,
#                         basename='djangofilter')  # /views/set/djangofiltering
mainapp_router.register('customtodofilter', mainapp.ToDoCustomDjangoFilterViewSet,
                        basename='custom')  # /views/set/customtodofilter,
mainapp_router.register('customprojectfilter', mainapp.ProjectCustomDjangoFilterViewSet,
                        basename='custom')  # /views/set/customprojectfilter,
mainapp_router.register('pagination', mainapp.ToDoLimitOffsetPaginatonViewSet,
                        basename='pagination')  # /views/set/pagination,

urlpatterns = [

    path('set/', include(mainapp_router.urls)),  # API Root

    path('todo/list/api/view/', mainapp.ToDoListAPIView.as_view()),
    path('todo/retrieve/api/view/<int:pk>/', mainapp.ToDoRetrieveAPIView.as_view()),
    path('todo/delete/api/view/<int:pk>/', mainapp.ToDoDeleteAPIView.as_view()),
    path('todo/update/api/view/<int:pk>/', mainapp.ToDoUpdateAPIView.as_view()),
    path('todo/create/api/view/', mainapp.ToDoCreateAPIView.as_view()),

    path('project/list/api/view/', mainapp.ProjectListAPIView.as_view()),
    path('project/retrieve/api/view/<int:pk>/', mainapp.ProjectRetrieveAPIView.as_view()),
    path('project/delete/api/view/<int:pk>/', mainapp.ProjectDeleteAPIView.as_view()),
    path('project/update/api/view/<int:pk>/', mainapp.ProjectUpdateAPIView.as_view()),
    path('project/create/api/view/', mainapp.ProjectCreateAPIView.as_view()),

    # path('todo/<str:text>/', mainapp.ToDoKwargsFilterView.as_view())  # views/todo/important/


]
