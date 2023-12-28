from rest_framework import serializers
from .models import * 

class ItemSerializer(serializers.ModelsSerializer):
    class Meta : 
        model = Items
        fields = ("desc", "rate", "quantity")

class InvoiceSerializer(serializers.ModelsSerializer):
    class Meta : 
        model = Invoices
        fields = "__all__"

class userSerializer(serializers.ModelsSerializer):
    class Meta:
        model = User
        fields = "__all__"