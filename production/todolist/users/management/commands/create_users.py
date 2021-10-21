from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        username = options['username']

        user = CustomUser.objects.create_superuser(username='django',
                                                   first_name=f'fname_{username}',
                                                   last_name=f'lname_{username}',
                                                   email=f'email_{username}@mail.com',
                                                   password='geekbrains',
                                                   is_superuser=True)
        print(f'superuser {user} created')

        CustomUser.objects.all().delete()
        count = options['count']
        for i in range(1, count + 1):
            user = CustomUser.objects.create_user(username=f'uname_{i}',
                                             first_name=f'fname_{i}',
                                             last_name=f'lname_{i}',
                                             email=f'email_{i}@mail.com')
            print(f'{user} created')
        print('done')
