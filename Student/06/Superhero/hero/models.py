from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField(default="None")
    strength = models.CharField(max_length=100, default="None")
    weakness = models.CharField(max_length=100, default="None")
    image = models.CharField(max_length=100, default="None")