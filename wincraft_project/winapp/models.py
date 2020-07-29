from django.db import models

# Create your models here.
class Queries(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    phone = models.PositiveIntegerField(blank=True,null=True)
    query = models.CharField(max_length=1000)
    
