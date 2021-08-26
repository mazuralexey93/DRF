from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import CustomUser


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
