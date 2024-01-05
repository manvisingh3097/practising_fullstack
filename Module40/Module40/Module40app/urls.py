from .views import *
from django.urls import path

urlpatterns = [
    path("range/", PriceRangeView.as_view(), name="Price-Range-View"),
    path("filter/", MultipleView.as_view(), name="Multiple-View"),
]
