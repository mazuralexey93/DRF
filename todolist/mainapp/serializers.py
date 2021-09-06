from rest_framework.relations import StringRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from mainapp.models import Project, ToDo
from users.serializers import CustomUserSerializer


class ProjectSerializer(ModelSerializer):
    users = CustomUserSerializer(many=True)
    # users = StringRelatedField(many=True)

    class Meta:
        model = Project
        # fields = ['name', 'users']
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = HyperlinkedIdentityField(view_name='project_details')
    user = HyperlinkedIdentityField(view_name='user_details')

    class Meta:
        model = ToDo
        # fields = ['name', 'link']
        fields = '__all__'
