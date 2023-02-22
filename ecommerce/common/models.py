from django.db import models
from ecommerceadmin.models import Products

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=10)

    class Meta:
        db_table = 'customer'

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'cart'
    