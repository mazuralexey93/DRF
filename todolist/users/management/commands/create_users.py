from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create users to test'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = CustomUser.objects.create(username=f'uname{i}', firstname=f'fname{i}',
                                             lastname=f'lname{i}', email=f'uname{i}@gmail.com')
            print(f'user {user} created')
        print('done')
