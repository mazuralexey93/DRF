from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        user = CustomUser.objects.create_superuser(username=f'{username}',
                                                   first_name=f'fname_{username}',
                                                   last_name=f'lname_{username}',
                                                   email=f'email_{username}@mail.com',
                                                   password='geekbrains')
        print(f'{user} created')

    print('done')
