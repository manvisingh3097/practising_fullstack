from django.urls import path
from .views import *

urlpatterns=[
    path("category/" , CategoryView.as_view(), name="category-view"),
    path("product/" , ProductView.as_view(), name="category-view"),
]