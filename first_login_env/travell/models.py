from django.db import models

# Create your models here.
class Destination(models.Model):
    # dynamic data connect with database (assign the variables so use = symbol)
    
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    caps = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    # dynamic data (field type give a colon symbol :)
    '''
    id : int
    name : str
    img : str
    desc : str
    caps : str
    price : int
    offer : bool
    '''
