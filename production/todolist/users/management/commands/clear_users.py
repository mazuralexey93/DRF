from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
