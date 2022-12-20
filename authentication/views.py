import email
from urllib import response
from venv import create
from . mail import send_otp
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
 
# API for sending OTP.   
class OTP_send(generics.CreateAPIView):
    serializer_class = OTP_Serializer
    
# OTP verification API.    
class Verify_OTP(generics.CreateAPIView):
    serializer_class = OTPVerifySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Email Verified'}, status=status.HTTP_200_OK)

# Registration API
class New_user_registration(generics.CreateAPIView):
    serializer_class = NewUserSerializer
    
# Login API
class Login(generics.CreateAPIView):
    serializer_class = LoginSerializer
