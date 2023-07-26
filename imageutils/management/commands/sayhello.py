from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Just Saying Hello'

    def add_arguments(self, parser):
        parser.add_argument('name',  help='Every friend has a name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        self.stdout.write("Hello "+name)

