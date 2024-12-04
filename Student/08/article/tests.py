from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Article

class ArticleAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)

class ArticleDataTest(TestCase):
    
    def test_article(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title='title 1')
        Article.objects.create(title='title 2')
        self.assertEqual(len(Article.objects.all()), 2)

        a = Article.objects.get(pk=2)
        self.assertEqual(a.title, 'title 2')

        a.title = "new title"
        a.save()
        self.assertEqual(a.title, 'new title')

        a.delete()
        self.assertEqual(len(Article.objects.all()), 1)

class ArticleViewsTest(TestCase):
    def test_article_list_view(self):
        self.assertEqual(reverse("article_list"),"/article/")
    
    def test_article_add_view(self):
        a = dict(title='T 1', body='None')
        b = dict(title='T 2', body='None')
        response = self.client.post(reverse("article_add"), a)
        response = self.client.post(reverse("article_add"), b)
        self.assertEqual(len(Article.objects.all()), 2)
        