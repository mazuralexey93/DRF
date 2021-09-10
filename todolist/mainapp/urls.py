from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

import mainapp.views as mainapp

mainapp_router = DefaultRouter()

mainapp_router.register('todos', mainapp.ToDoViewSet,
                        basename='todo')  # /views/set/todos
mainapp_router.register('filtering', mainapp.ToDoQuerySetFilterViewSet,
                        basename='filter')  # /views/set/filtering
mainapp_router.register('djangofiltering', mainapp.ArticleDjangoFilterViewSet,
                        basename='djangofilter')  # /views/set/djangofiltering
mainapp_router.register('customfilter', mainapp.ArticleCustomDjangoFilterViewSet,
                        basename='custom')  # /views/set/customfilter,
mainapp_router.register('pagination', mainapp.ArticleLimitOffsetPaginatonViewSet,
                        basename='pagination')  # /views/set/pagination,

urlpatterns = [

    path('set/', include(mainapp_router.urls)),  # API Root

    path('todo/list/api/view/', mainapp.ToDoListAPIView.as_view()),
    path('todo/retrieve/api/view/<int:pk>/', mainapp.ToDoRetrieveAPIView.as_view()),
    path('todo/delete/api/view/<int:pk>/', mainapp.ToDoDeleteAPIView.as_view()),
    path('todo/update/api/view/<int:pk>/', mainapp.ToDoUpdateAPIView.as_view()),
    path('todo/create/api/view/', mainapp.ToDoCreateAPIView.as_view()),


    path('todo/<str:text>/', mainapp.ToDoKwargsFilterView.as_view())  # views/todo/important/


]
