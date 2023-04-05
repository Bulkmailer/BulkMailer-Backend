from platform import machine
from rest_framework import generics,status,mixins
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
 
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
    

# Password OTP view 

class Reset_Password_OTP_View(generics.CreateAPIView):
    serializer_class = ResetPasswordViewOTPSerializer

# Reset Password API
class Password_Change_View(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = ChangePasswordSerializer
    
    def get_object(self):

        email = self.request.data.get('email')
        user = New_User_Resgistration.objects.get(email=email)
        return user
    
    def patch(self, request, *args, **kwargs):
        self.update(request,*args, **kwargs)
        return Response({'msg':'Password Change Successfullly'},status=status.HTTP_200_OK)

# Gmail APP Password Add and get APIs
class Add_Gmail_Pass(generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView):
    serializer_class = GmailAPPModelSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Gmail_APP_Model.objects.filter(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['user'] = request.user.id
        return self.create(request)
        

# Gmail APP Password Update API
class Update_APP_Password(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = UpdateAppPassword
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        email = self.request.data.get('email')
        app_pass = Gmail_APP_Model.objects.get(email=email)
        return app_pass
    
    def patch(self, request, *args, **kwargs):
        self.update(request,*args, **kwargs)
        return Response({'msg':'APP Password Change Successfullly'},status=status.HTTP_200_OK)

#Profile Details Get and Update APIs

class Profile_details(generics.ListAPIView, mixins.UpdateModelMixin):
    serializer_class = ProfileDetailsUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        user = New_User_Resgistration.objects.get(id=self.request.user.id)
        return user
    
    def get_queryset(self):
        return New_User_Resgistration.objects.filter(id=self.request.user.id)
    
    def patch(self, request, *args, **kwargs):
        self.update(request,*args, **kwargs)
        return Response({"status": "Profile Updated Successfully."}, status=status.HTTP_200_OK)
        

       
    