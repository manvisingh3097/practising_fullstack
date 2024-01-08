from .views import * 
from django.urls import path

urlpatterns = [
    path("productsview/", ProductsView.as_view(), name="Products-View"),
    # path("allproducts/", MultipleView.as_view(), name="Multiple-View"),
    # path("filterview/", FilterView.as_view(), name="Filter-View"),
    path("signup/", SignupView.as_view(), name="Signup-View"),
    path("login/", LoginView.as_view(), name="Login-View"),
]