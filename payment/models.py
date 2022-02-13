from django.db import models
import datetime



# Create your models here.
class Payment(models.Model):
    first_name = models.CharField( max_length=12, null=True)

    last_name = models.CharField(max_length=15, null=True)

    plate_number =models.CharField(max_length=15, null=True)

    date = models.DateField(max_length=27, null=True)

    time_in=models.CharField(max_length=10, null=True)  

    time_out=models.CharField(max_length=10, null=True)  