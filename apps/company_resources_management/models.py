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
    


class Expense(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True, verbose_name="Date issued")
    price = models.FloatField(verbose_name="Amount due")
    invoice_description = models.TextField(verbose_name="Invoice description")
    paid_to = models.CharField(max_length=255, verbose_name="Paid to")


    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    
    def __str__(self):
        return f"New Expense from {self.created_by.first_name} -- {self.paid_to}"
    

class IncomeSource(models.Model):
    name = models.CharField(max_length=255, verbose_name="Income source name")
    description = models.TextField(verbose_name="Income source description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Income source"
        verbose_name_plural = "Income sources"
    

    def __str__(self):
        return self.name




class Earning(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_recieved = models.DateTimeField(auto_now_add=True, verbose_name="Date issued")
    price = models.FloatField(verbose_name="Amount due")
    income_source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE, verbose_name="Related income source") 

    class Meta:
        verbose_name = "Earning"
        verbose_name_plural = "Earnings"

    def __str__(self):
        return f"New earning from {self.income_source.name}"