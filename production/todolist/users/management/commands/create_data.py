import random

from django.core.management.base import BaseCommand
from mainapp.models import ToDo, Project
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create test data'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('users_count', type=int)
        parser.add_argument('project_count', type=int)
        parser.add_argument('todo_count', type=int)


    def handle(self, *args, **options):

        CustomUser.objects.all().delete()
        Project.objects.all().delete()
        ToDo.objects.all().delete()

        username = options['username']

        user = CustomUser.objects.create_superuser(username='django',
                                                   first_name=f'fname_{username}',
                                                   last_name=f'lname_{username}',
                                                   email=f'email_{username}@mail.com',
                                                   password='geekbrains')
        print(f'superuser {user} created')

        users_count = options['users_count']
        for i in range(1, users_count + 1):
            user = CustomUser.objects.create_user(username=f'uname_{i}',
                                                  first_name=f'fname_{i}',
                                                  last_name=f'lname_{i}',
                                                  email=f'email_{i}@mail.com')
            print(f'{user} created')
        print('done')

        users = CustomUser.objects.all()
        # Project.objects.all().delete()
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

        # ToDo.objects.all().delete()
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
