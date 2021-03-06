import graphene
from graphene import Mutation
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
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    todos_by_project_name = graphene.List(TodoType, name=graphene.String(required=False))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_users(self, info):
        return CustomUser.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_user_by_id(self, info, id):
        return CustomUser.objects.get(id=id)


    def resolve_todos_by_project_name(self, info, name=None):
        todos = ToDo.objects.all()
        if name:
            todos = todos.filter(project__name=name)
        return todos


class ProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, id):
        project = Project.objects.get(pk=id)
        project.name = name
        project.save()
        return ProjectMutation(project=project)


class Mutation(graphene.ObjectType):
    update_project = ProjectMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
