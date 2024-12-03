from django.core.management.base import BaseCommand
from requests import get

class Command(BaseCommand):

    def handle(self, *args, **options):
        word = get('https://shrinking-world.com')
        print('Google', word)
        print(word.text)

        