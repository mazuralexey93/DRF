from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from users.models import CustomUser


# class UserSerializer(HyperlinkedModelSerializer):
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
