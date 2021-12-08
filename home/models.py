from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone = models.CharField(max_length=15)
    cnic = models.CharField(max_length=20)
    username = models.CharField(primary_key=True, max_length=122)



class Contact(models.Model):
    name = models.CharField(max_length=122, null = True)
    email =models.CharField(max_length=122, null = True)
    message=models.TextField(null = True)



class Account(models.Model):
    Accno = models.IntegerField(primary_key=True)
    Owner = models.ForeignKey(customer, on_delete=models.CASCADE,)
    Balance = models.FloatField(default=0)