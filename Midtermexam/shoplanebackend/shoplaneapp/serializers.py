from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"

class ProductSeializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

