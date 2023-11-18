from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class CategoryView(APIView):
    def post(self,request):
        try:

            data = request.data
            print(data)
            category.objects.create(name = data["name"])
# to use json into keyword argument we use **
            return Response({"message":"category has beencreated"},status=201)
        except:
            return Response({"message": "Incorrect data"}, status=400)
        
    def get(self,request):
        categories = category.object.all().values()
        return Response(list(categories) , status=200)



