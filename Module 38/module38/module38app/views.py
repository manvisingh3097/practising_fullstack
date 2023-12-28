from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class ProductReview(APIView):
    def get(self,request,product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product).data
        return Response(serializer)
    
class OrderDetails(APIView):
    def get(self,request,order_id):
        order = Product.objects.get(id=order_id)
        serializer = OrderSerializer(order).data
        return Response(serializer)
    
        