from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_Permissions import IsAuthenticated
from .serializers import *
from .data import *

# Create your views here.

class SignupView(APIView):
    def post(self, request):
        data = request.data
        data["user_id"] = len(user_data) + 1
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            user_data.append(serializer.data)
            return Response({"message"  "Account has been created"}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        for val in user_data:
            if val['email'] == data['email'] and val['password'] == data['password']:
                token = jwt.encode({"test": "this is jwt testing"}, "secret", algorithm="HS256")
                return Response ({"message": "Login success.", "token": str(token)}, status=200)
        return Response({"message": "Email or password does not match"}, status=401)
    
    class InvoiceView(APIView):
        Permission_classes = []