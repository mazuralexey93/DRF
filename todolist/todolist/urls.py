from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.views import CustomUserViewSet

router = DefaultRouter()
router.register('users', CustomUserViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    path('views/', include('mainapp.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),

]
