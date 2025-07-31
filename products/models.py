from django.db import models


from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
