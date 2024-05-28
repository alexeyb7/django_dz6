from django.core.management.base import BaseCommand
from myshop.models import Client


class Command(BaseCommand):
    help = 'Create a client'

    def handle(self, *args, **options):
        client = Client(name='First', email='aa@aa.aa', phone='123-456-789', address='test address')
        client.save()
        self.stdout.write(f'{client}')
        self.stdout.write(self.style.SUCCESS('Successfully created client'))

        client = Client(name='Second', email='bb@bb.bb', phone='233-456-789', address='test2 address')
        client.save()
        self.stdout.write(f'{client}')
        self.stdout.write(self.style.SUCCESS('Successfully created client'))
