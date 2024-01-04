from django.db import models

# Create your models here.

class User(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    Email = models.EmailField(max_length=200,unique=True)
    mobile_number = models.IntegerField()
    Password = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE, related_name="orders")
    order_number = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True , blank=True , default=None)
    shipping = models.CharField(max_length=200 ,null=True , default=None)
    Description = models.TextField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=300)
    Brand = models.CharField(max_length=200)
    featured = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name="order_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_item")
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="product_review")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    rate = models.IntegerField()
    review = models.TextField() 
    created = models.DateField(auto_now_add=True)

class BillingAddress(models.Model):
    order=models.OneToOneField(Order, on_delete= models.CASCADE, related_name="billing")
    address = models.TextField()
    city = models.CharField(max_length=200)

class Coupon(models.Model):
    code = models.CharField(max_length=8)
    discount = models.IntegerField(Order)
    order = models.ManyToManyField(Order)