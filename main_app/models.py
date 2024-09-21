from django.db import models


SIZES= (
    ('S', 'small'),
    ('M', 'medium'),
    ('L', 'large')
)
# Create your models here.

class Rock(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default= SIZES[0][0]

    )

    def __str__(self):
        return self.name