from django.db import models

# Create your models here.  
class prem(models.Model):
    firstname = models.CharField(max_length=100) 
    lastname = models.CharField(max_length=100)
    ph = models.CharField(max_length=100)