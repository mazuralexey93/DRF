from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    # path('todo/list/api/view/', mainapp.ToDoAPIView.as_view()),
    path('todo/list/api/view/', mainapp.ToDoListAPIView.as_view()),
    path('todo/retrieve/api/view/<int:pk>/', mainapp.ToDoRetrieveAPIView.as_view()),
    path('todo/delete/api/view/<int:pk>/', mainapp.ToDoDeleteAPIView.as_view()),
    path('todo/update/api/view/<int:pk>/', mainapp.ToDoUpdateAPIView.as_view()),
    path('todo/create/api/view/', mainapp.ToDoCreateAPIView.as_view()),
]