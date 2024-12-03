from django.test import SimpleTestCase, TestCase
from .models import Article

class ArticleAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)

class ArticleDataTest(TestCase):
    
    def test_article(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title='title 1')
        Article.objects.create(title='title 2')
        self.assertEqual(len(Article.objects.all()), 1)