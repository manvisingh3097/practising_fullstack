from django.db import models

# Create your models here.

class User(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    Email = models.EmailField(max_length=200,unique=True)
    mobile_number = models.Model(max_length=15)
    Password = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE, related_name="orders")
    order_number = models.IntegerField(max_length=200)
    order_date = models.DateField(auto_add_now=True)

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True  blank=True)
    shipping = models.CharField(max_length=200 ,null=True default=None)
    Description = models.TextField()
    price = models.FloatField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=30)
    Brand = models.CharField(max_length=True)
    featured = models.CharField(default=True)
    active = models



class Orderitem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

class Review(models.Model):
    rate = models.SmallIntegerField()
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    Product = models.CharField()
    Created_at = models.DateField()
    active = models.DateField()

