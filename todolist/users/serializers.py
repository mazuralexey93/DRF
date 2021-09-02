from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from mainapp import serializers
from users.models import CustomUser, CustomUserRole


class CustomUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomUserSRoleSerializer(serializers.ModelSerializer):
    model = CustomUserRole
    role = serializers.CharField(max_length=128)
    user = CustomUserSerializer()
