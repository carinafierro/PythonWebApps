from django.test import TestCase
from hero.models import Investigator, Superhero, Article

class InvestigatorTest(TestCase):
    def investigatortest(self):
        investigator = Investigator.objects.create(name="Natasha")
        self.assertEqual(investigator.name, "Natasha")

class ArticleTest(TestCase):
    def articletest(self):
        article = Article.objects.create(title="Heroes")
        self.assertEqual(article.title, "Heroes")

class SuperheroTest(TestCase):
    def superherotest(self):
        superhero = Superhero.objects.create(name="batman")
        self.assertEqual(superhero.identity, "Bruce Wayne")