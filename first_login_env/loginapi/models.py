from django.db import models

# Create your models here.
class Empapi(models.Model):
    
    firstname = models.CharField(max_length=200),
    lastname = models.CharField(max_length=200),
    email = models.CharField(max_length=200),
    password = models.CharField(max_length=200),
   