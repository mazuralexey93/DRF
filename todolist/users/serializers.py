from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from users.models import CustomUser


# class UserSerializer(HyperlinkedModelSerializer):
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
