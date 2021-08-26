from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import CustomUser


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' # ?


