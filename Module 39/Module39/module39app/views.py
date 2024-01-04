from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .models import *
from .serializers import *

# Create your views here.


def SearchApi(APIView):
    def get(self, request):
        para = request.GET.get("query" , None)
        products = Product.objects.all()
        serializer =  ProductSerializer(products, many=True).data
        return Response(serializer)

def FilterApi(APIView):
    def get(self, request):
        brand = request.GET.get("brand", None)
        cat = request.GET.get('cat', None)
        minRange = request.GET.get("min" , None)
        maxRange = request.GET.get("max" , None)
        products = Product.odjects.all()
        if brand:
            products = products.filter(brand_iexact=brand)
        if cat:
            products = products.filter(category_iexact=cat)
        if minRange:
            products = products.filter(price_gte=minRange)
        if maxRange:
            products = products.filter(price_lte=maxRange)
        serializer = ProductSerializer(products, many=True).data
        return Response(serializer)

class PaginationView(APIView):
    def get(self, request):
        page_no = int(request.GET.get("page", 1))
        products = Product.objects.all().order_by("id")
        paginate = Paginator(products, 5)
        page = paginate.get_page(page_no)
        serializer = ProductSerializer(page.object_list, many=True).data
        return Response(
            {
                "data": serializer,
                "pages": paginate.num_pages,
                "item_count": products.count(),
            }
        )
