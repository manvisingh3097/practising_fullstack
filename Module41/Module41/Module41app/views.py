from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Sum

# Create your views here.

class PriceRangeView(APIView):
    def get(self , request):
        minPrice = request.GET.get("min" , None)
        maxPrice = request.GET.get("min" , None)
        if maxPrice and minPrice  :
            product = Product.objects.filter(Q(price__gt=int(minPrice)) & Q(price__lt=int(maxPrice)))
            serializer = ProductSerializer(product, many=True).data
            return Response (serializer, status=200)
        return Response({"message": "min and max parameters are required"}, status=400)    


class MultipleView(APIView):
    def get(self, request):
        cat = request.GET.get("cat", None)
        brand = request.GET.get("brand", None)
        active = request.GET.get("active", None)
        products = products.objects.all()
        if cat:
            products = products.filter(category__iexact=cat)
        if brand:
            products = products.filter(brand__iexact=brand)
        if active:
            products = products.filter(active_in=[True])
        serializer = ProductSerializer(products, many=True).data
        return Response(serializer, status=200)
    
class MultipleView(APIView):
    def get(self, request):
        para = request.GET.get("para", None)
        products = Product.objects.filter(Q(name__icontains=para) | Q(description__icontais=para))
        serializer = ProductSerializer(products, many=True).data
        return Response(serializer, status=200)

class SignupView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created succesfully"},status=201)
        return Response(serializer.errors, status=400)
    
class LoginView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializers.is_valid:
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            return Response(
                {
                    "message": "Login succesfull",
                    "access_token": str(token.access_token),
                    "refresh_token": str(token),
                }
            )
        return Response(serializer.errors, status=401)