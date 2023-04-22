from django.db import models

# Create your models here.
#class position(models.Model):
 #       title= models.CharField(max_length=100)
class credentials(models.Model):
  #      position = models.ForeignKey(position,on_delete=models.CASCADE)
        username = models.CharField(max_length=200)
        fname    = models.CharField(max_length=200)
        lname    = models.CharField(max_length=200)
        email    = models.CharField(max_length=200)
        pass1    = models.CharField(max_length=200)
        pass2    = models.CharField(max_length=200)
        

       