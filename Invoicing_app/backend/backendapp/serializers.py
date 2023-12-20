from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelsSerializer):
    class Meta:
        model = 