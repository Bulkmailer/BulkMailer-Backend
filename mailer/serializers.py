# from dataclasses import fields
# import email
# from .models import *
# from django.core.exceptions import ValidationError
# from rest_framework import serializers
# import pandas as pd

# class CreateGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Groups
#         fields = '__all__'
        

# class BulkDataADD(serializers.Serializer):
#     file = serializers.FileField()
#     group = serializers.IntegerField()
    
#     extra_kwargs = {'file': {'required': True}, 'group': {'required': True}}
    
#     def create(self, validated_data):
#         data = pd.read_csv(validated_data['file'])
#         file = data.to_csv().strip()
#         file = file.split('\n')[1:]
        
#         emailList = []
#         for e in file:
#             e = e.split(',')[1:]
#             emailList.append({"name":e[0],"email":e[2]})
#         group = Groups.objects.get(id=validated_data['group'])
#         create = [Group_Details(group=group,email=e['email'],name=e['name']) for e in emailList]
#         Group_Details.objects.bulk_create(create)
        
#         return validated_data
            
