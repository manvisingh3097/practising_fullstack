from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField (write_only=True)

    class Meta:

        model = User

        fields = ('username','password')

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
        