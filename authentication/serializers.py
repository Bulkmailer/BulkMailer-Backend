import email
import re
from rest_framework.serializers import ModelSerializer
from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers



class OTP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email']

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_User_Resgistration
        fields = ["id","name","user_name", "email", "password"]
        extra_kwargs={
            'password':{'write_only': True},
        }
    
        
        