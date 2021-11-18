from django.db import models

# Create your models here.
class customer(models.Model):
    
    name = models.CharField(max_length=122, null = True)
    email =models.CharField(max_length=122, null = True)
    phone = models.CharField(max_length=15, null= True)
    cnic = models.CharField(max_length=122, null = True)
    password =models.CharField(max_length=122, null = True)

    def __str__(self):
        return self.email



class Contact(models.Model):
    name = models.CharField(max_length=122, null = True)
    email =models.CharField(max_length=122, null = True)
    message=models.TextField(null = True)

    def __str__(self):
        return self.name
