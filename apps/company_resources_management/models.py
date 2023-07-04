from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    subscription_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name