from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers
import pandas as pd

class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'
        
            
