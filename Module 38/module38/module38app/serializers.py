from rest_framework import serializers
from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product' , 'user')

class ProductSerializer(serializers.ModelSerializer):
    product_review = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = ('__all__')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderitem
        fields = ('__all__')  

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ('__all__')       