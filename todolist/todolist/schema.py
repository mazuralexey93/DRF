import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Project, ToDo
from users.models import CustomUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    all_todos = graphene.List(TodoType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_users(self, info):
        return CustomUser.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query)
