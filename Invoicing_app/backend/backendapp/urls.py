from django.urls import path 
from .views import *

urlpatterns = [
    path("user/signup/", SignupView.as_view(), name="signup"),
    path("user/login/", LoginView.as_view(), name="login"),
]