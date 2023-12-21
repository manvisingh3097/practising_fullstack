from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class CategoryView(APIView):
    def post(self,request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Category has been created successfully"},status=201)
        return  Response(serializer.errors, status=400)
    
        
# to use json into keyword argument we use **       
        
    def get(self,request):
        categories = category.objects.all()
        serializer = CategorySerializer(categories, many=True).data
        return Response(serializer , status=200)
    

class ProductView(APIView):
    def post(self,request):
        try: 
            data = request.data
            Product.objects.create(
                name=data["name"],
                description =data["description"],
                image=data["image"],
                price=data["price"],

        )
            
            return Response({"message:" "product created"},status=201)
        except:
            return Response({"message:" "bad request"} ,status=400)

    def get(self,request):
        product=  Product.objects.all().values()
        return Response(list(product), status=200)


