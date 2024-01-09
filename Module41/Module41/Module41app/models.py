from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields): 
        if not username:
            raise ValueError("username is required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
        



class User(AbstractBaseUser):
    name = models.CharField(max_length=200 , default="")
    username = models.CharField(max_length=200, unique=True)
    # Email = models.EmailField(max_length=200,unique=True)
    Password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    objects=UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    def has_module_perms(self, app_label):
        return self.is_superuser


class Order(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE, related_name="orders")
    order_number = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(null=True , blank=True , default=None)
    shipping = models.CharField(max_length=200 ,null=True , default=None)
    description = models.TextField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=300)
    brand = models.CharField(max_length=200)
    featured = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_review = models.FloatField(default=0.00)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='name-index'),
            models.Index(fields=['category', 'brand'], name='cat-brand-index'),
            ]


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