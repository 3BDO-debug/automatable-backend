from django.db import models
from accounts.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    subscription_cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Expenses(models.Model):
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_description = models.TextField()
    paid_to = models.CharField(max_length=255)
    
    
    
    
class IncomeSource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Income(models.Model):
    recevied_at = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField()
    income_source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE)