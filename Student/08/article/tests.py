from django.test import SimpleTestCase, TestCase
from .models import Article

class ArticleAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)

class ArticleDataTest(TestCase):
    
    def test_article(self):
        Article.objects.create(title='title')
        self.assertEqual(len(Article.objects.all()), 1)