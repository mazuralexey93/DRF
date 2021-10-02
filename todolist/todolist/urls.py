from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from mainapp.views import ToDoViewSet, ProjectViewSet
from users.views import CustomUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    title="TODO API",
    permission_classes=[IsAuthenticatedOrReadOnly],
)

router = DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('todos', ToDoViewSet)
router.register('projects', ProjectViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    re_path(r'^api/(?P<version>\d\.\d)/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', schema_view)

]
