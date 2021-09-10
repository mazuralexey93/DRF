from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.views import CustomUserViewSet

users_router = DefaultRouter()
users_router.register('users', CustomUserViewSet)  # api/users/


urlpatterns = [

    path('api/', include(users_router.urls)),
    path('views/', include('mainapp.urls')),
    path('admin/', admin.site.urls),

]
