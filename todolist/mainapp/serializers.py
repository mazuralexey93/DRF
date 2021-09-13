from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from mainapp.models import Project, ToDo


class ProjectSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = StringRelatedField()
    user = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
