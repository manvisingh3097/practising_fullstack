from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product' , 'user')

class ProductSerializer(serializers.ModelSerializer):
    
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

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField (write_only=True)

    class Meta:

        model = User

        fields = ('name','username','username', 'email')

    def create(self, validated_data):

        user = User.objects.create_user(

        username=validated_data['username'],

        password=validated_data['password']

        )

        return user 
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("username or password does not match.")
        