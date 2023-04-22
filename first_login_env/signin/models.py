from django.db import models

# Create your models here.
class userlogin(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmpassword = models.CharField(max_length=200)
    mfileupload = models.FileField(upload_to='file')
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    secondaddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=8)
    grid = models.BooleanField(default=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name