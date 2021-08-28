from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        for i in range(1, count + 1):
            user = CustomUser.objects.create_user(username=f'uname_{i}',
                                             first_name=f'fname_{i}',
                                             last_name=f'lname_{i}',
                                             email=f'email_{i}@mail.com')
            print(f'{user} created')
        print('done')
