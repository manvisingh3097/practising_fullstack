from django.db import models

# Create your models here.

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    
class Product(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    Description = models.TextField(null=True , blank=True,default=None)
    image = models.URLField(null=True , blank=True , default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
