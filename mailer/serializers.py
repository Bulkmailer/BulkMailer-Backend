from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers

class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'
    
    def validate(self, attrs):
        groupName = attrs['name']
        user = attrs['user']
        
        groups = Groups.objects.filter(user=user)
        
        if groups.filter(name=groupName).exists():
            raise ValidationError(
                {'msg':'Group with this name already exists'}
            )
        return attrs

class ViewGroupDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_Details
        fields = '__all__'
    


class AddContactsManuallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_Details
        fields = '__all__'

        

            
