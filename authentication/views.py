import email
from urllib import response
from venv import create
from . mail import send_otp
from rest_framework import generics,status
from rest_framework.response import Response
from datetime import timedelta
from rest_framework.views import APIView
from . models import *
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

def getTokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
 
# OTP verification API.   
class OTP_send(generics.CreateAPIView):
    serializer_class = OTP_Serializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_otp(serializer.data['email'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# OTP verification API.    
class Verify_OTP(generics.CreateAPIView):
    def post(self,request):
        email = self.request.data.get('email')
        otp = self.request.data.get('otp')
        
        userOTP = OTP.objects.get(email = email)
        
        if not userOTP.otp == otp:
            context = {'msg':'otp is not valid'}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        if userOTP.time + timedelta(minutes=3) < timezone.now():
            message = {'msg':'OTP expired'}
            userOTP.delete()
            return Response(message,status=status.HTTP_403_FORBIDDEN)
        userOTP.delete()
        return Response({'msg':'Email verified'}, status=status.HTTP_200_OK) 

# Registration API
class New_user_registration(APIView):
    def post(self,request):
        serializer = NewUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = New_User_Resgistration.objects.get(email=serializer.data['email'])
            user.password = make_password(serializer.data['password'])
            user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# Login API

class Login(generics.CreateAPIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
            
        user = New_User_Resgistration.objects.filter(email = email)
        if not user.exists():
            context = {'msg':'user with this mail does not exist'}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if user is not None:
            token = getTokens(user)
            return Response({'email':user.email,'token': token,'msg':'Login Success'}, status=status.HTTP_200_OK)

        return Response({'msg':'Enter correct Password'}, status=status.HTTP_400_BAD_REQUEST)
