from django.db import models

class User(models.Model):
   Email= models.EmailField( max_length=254)
   Password=models.CharField(max_length=500)