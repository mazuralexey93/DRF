import random

from django.core.management.base import BaseCommand
from mainapp.models import ToDo, Project
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create projects and todos'

    def add_arguments(self, parser):
        parser.add_argument('project_count', type=int)
        parser.add_argument('todo_count', type=int)

    def handle(self, *args, **options):
        users = CustomUser.objects.all()

        Project.objects.all().delete()
        project_count = options['project_count']
        project_list = []
        for i in range(project_count):
            project = Project.objects.create(name=f'project{i}',
                                             link=f'http://localhost/projects/project/{i}/')
            for _ in range(random.randrange(5)):
                project.users.add(random.choice(users))
            project.save()
            project_list.append(project)
        print(f'{project_count} projects created')

        ToDo.objects.all().delete()
        todo_count = options['todo_count']
        superuser = CustomUser.objects.filter(is_superuser=True).first()
        if superuser:
            for i in range(todo_count):
                project = random.choice(project_list)
                ToDo.objects.create(project=project, text=f'Important todo number {i}',
                                    user=random.choice(users))
            print(f'{todo_count} todos created')
        else:
            print('Superuser not found, program not able to create todos!')
