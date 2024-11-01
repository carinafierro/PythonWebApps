from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)  # URL or path for the image

    def __str__(self):
        return self.name