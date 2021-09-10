from django.urls import path, include
from rest_framework.routers import DefaultRouter

import mainapp.views as mainapp

mainapp_router = DefaultRouter()

mainapp_router.register('todos', mainapp.ToDoViewSet,
                        basename='todo')  # /views/set/todos
mainapp_router.register('projects', mainapp.ProjectViewSet,
                        basename='project')  # /views/set/projects

urlpatterns = [
    path('set/', include(mainapp_router.urls)),  # API Root

]
