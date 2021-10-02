from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class CustomUserBaseSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        ordering = ['pk']
        fields = ['username', 'email', ]


class CustomUserSerializer(CustomUserBaseSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
