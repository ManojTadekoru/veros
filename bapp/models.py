from django.db import models

# Create your models here.
class details(models.Model):
    email=models.EmailField(unique=True,max_length=50)
    password=models.CharField(max_length=30)

class transaction(models.Model):
    serviceid=models.CharField(max_length=30)
    objectid=models.CharField(max_length=30)
    transactionid=models.CharField(max_length=30)
    transactiondate=models.DateField()
    transactiontime=models.TimeField()
    status=models.CharField(max_length=30)
    message=models.CharField(max_length=30)
    responsecode=models.BigIntegerField()
