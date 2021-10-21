from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)


    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        username = options['username']

        user = CustomUser.objects.create_superuser(username='django',
                                                   first_name=f'fname_{username}',
                                                   last_name=f'lname_{username}',
                                                   email=f'email_{username}@mail.com',
                                                   password='geekbrains',
                                                   is_superuser=True)
        # user = CustomUser.objects.create_superuser('django', 'djangoadmin@mail.ru', 'geekbrains')
        print(f'{user} created')

    print('done')
