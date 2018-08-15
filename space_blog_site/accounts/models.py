from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length = 100)
    cust_auth = models.BooleanField()
