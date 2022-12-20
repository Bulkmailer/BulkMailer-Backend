import re
from rest_framework.serializers import ModelSerializer
from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers
from . mail import send_otp
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate



class OTP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email']
    
    def validate(self,data):
        email = data['email']
        if not re.findall('@.', email):
            raise ValidationError(
                ("Enter a valid email")
            )
        return data
    
    def create(self, data):
        userOTP = OTP.objects.filter(email=data["email"])
        if userOTP is not None:
            print(userOTP)
            userOTP.delete()
        email = data['email']
        OTP.objects.create(email=email)
        send_otp(email)
        
        return data

class OTPVerifySerializer(serializers.Serializer):
    email = serializers.CharField(write_only=True)
    otp = serializers.CharField(write_only=True)
    def validate(self, data):
        userOTP = OTP.objects.get(email = data['email'])
        
        if not userOTP.otp == data['otp']:
            context = {'msg':'otp is not valid'}
            raise ValidationError(
                (context)
            )
        if userOTP.time + timedelta(minutes=3) < timezone.now():
            context = {'msg':'OTP expired'}
            userOTP.delete()
            context = {'msg':'otp is not valid'}
            raise ValidationError(
                (context)
            )
        userOTP.delete()
        return {
            'msg':'done'
        }
        
    def create(self, validated_data):
        return validated_data
        

       
        
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_User_Resgistration
        fields = ["id","name","user_name", "email", "password"]
        extra_kwargs={
            'password':{'write_only': True},
        }
        
    def validate_password(self,data):
            if len(data) < 8 or not re.findall('\d', data) or not re.findall('[A-Z]', data) or not re.findall('[a-z]', data) or not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', data):
                raise ValidationError(
                    ("The password needs to be more than 8 characters, contain atleast one uppercase,one lowercase and a special character")
                )

            return data
    def create(self, data):
            user = New_User_Resgistration.objects.create(name=data['name'],user_name=data['user_name'],email=data['email'],password=data['password'])
            user.password = make_password(data['password'])
            user.is_active = True
            user.save()
            return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    
        
    def validate(self,data):
        
        user = authenticate(email=data['email'],password=data['password'])
        
        if not user:
            raise ValidationError(
                'User does not exists'
            )
        data['refresh'] = user.refresh
        data['access'] = user.access
        return data
        
    def create(self, validated_data):
        return validated_data
            
        