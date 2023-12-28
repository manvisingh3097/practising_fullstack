from .views import *
from django.urls import path

urlpatterns=[
    path("review/<int:product_id>/", ProductReview.as_view(),name="Product_Review"),
    path("order/<int:order_id>/", OrderDetails.as_view(),name="Order_Details"),
]