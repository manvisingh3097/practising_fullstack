from .views import *
from django.urls import path

urlpatterns=[
    path("search/", SearchApi.as_view(),name="Search_View"),
    path("filter/", FilterApi.as_view(),name="Order_Details"),
    path("paginator/", PaginationView.as_view(),name="Page_details"),
]