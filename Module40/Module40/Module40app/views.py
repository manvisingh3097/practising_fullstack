from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Sum
from .serializers import *

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