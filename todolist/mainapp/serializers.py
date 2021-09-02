from rest_framework import serializers

from mainapp.models import Project, ToDo
from users.serializers import CustomUserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    model = Project
    name = serializers.CharField(max_length=128)
    users = CustomUserSerializer(many=True)


class ToDoSerializer(serializers.ModelSerializer):
    model = ToDo
    name = serializers.CharField(max_length=128)
    creator = CustomUserSerializer()
