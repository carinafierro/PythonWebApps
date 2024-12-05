from django.test import TestCase
from hero.models import Investigator, Superhero, Article

class Test(TestCase):
    def investigatortest(self):
        investigator = Investigator.objects.create(name="")