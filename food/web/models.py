from django.db import models

# Create your models here.
class Customer(models.Model):
    cname = models.CharField(max_length=30)
    cuname = models.CharField(primary_key=True, max_length=10)
    dob = models.DateField()