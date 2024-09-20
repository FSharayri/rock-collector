from django.db import models

# Create your models here.

class Rock(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    size = models.CharField(max_length=30)
    def __str__(self):
        return self.name