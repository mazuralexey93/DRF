from rest_framework.relations import StringRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from mainapp.models import Project, ToDo
from users.serializers import CustomUserSerializer


class ProjectSerializer(ModelSerializer):
    users = CustomUserSerializer(many=True)
    # users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = StringRelatedField()
    user = StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
