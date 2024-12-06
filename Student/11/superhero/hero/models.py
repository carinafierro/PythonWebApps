from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    doc = models.CharField(max_length=200, default='Documents')
    cover_image = models.CharField(max_length=200, null=True, blank=True)


books = Book.object.all().values()

for book in books:
    print(book)