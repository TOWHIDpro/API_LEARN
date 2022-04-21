from pyexpat import model
from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disc = models.TextField()
    
    def __str__(self):
        return self.name