from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
