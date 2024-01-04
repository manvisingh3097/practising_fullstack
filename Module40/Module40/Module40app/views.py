from django.shortcuts import render

# Create your views here.

class PriceRangeView(APIView):
    def get(self , request):
        minPrice = request.GET.get("min" , None)