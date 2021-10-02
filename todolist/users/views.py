from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from users.models import CustomUser
from users.serializers import CustomUserSerializer, CustomUserBaseSerializer


class CustomUserViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        super(CustomUserViewSet).create(request)

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return CustomUserBaseSerializer
        return CustomUserSerializer
