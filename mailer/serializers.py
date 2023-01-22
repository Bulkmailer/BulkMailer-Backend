from dataclasses import field
from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers
from authentication.task import *
import pytz
from datetime import datetime

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
    
    def validate(self, data):
        email = data['email']
        group_details = Group_Details.objects.filter(group=data['group'])
 
        
        if  group_details.filter(email=email).exists():
            raise ValidationError(
                {'msg':'email already exists in this group'}
            )
        
        return data

class MassMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentMail
        fields = ['id','user','_from','_group','_company','_body','_subject','_file','_template','status','celeryID']
    
    def create(self, data):
        mail = SentMail.objects.create(**data)
        file_path = f'{mail._file.name}'
        celeryIDD = send_custom_mass_mail.apply_async(args = [mail._from,mail._group,mail._subject,mail._company,mail._body,file_path,mail._template])
        mail.celeryID = celeryIDD.id
        mail.status = celeryIDD.status
        print(celeryIDD)
        print(celeryIDD.status)
        print(celeryIDD.id)
        mail.save()
        return data
        
class ScheduleMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulingMail
        fields = ['id','user','_from','_group','_company','_body','_subject','_file','_template','_year','_month','_date','_hour','_minute','status','celeryID']
    def create(self, data):
        mail = SchedulingMail.objects.create(**data)
        file_path = f'{mail._file.name}'
        asia_tz = pytz.timezone('Asia/kolkata')
        asia_dt = asia_tz.localize(datetime(data['_year'], data['_month'], data['_date'], data['_hour'], data['_minute']))
        etaTimezone = asia_dt.astimezone(pytz.UTC)
        celeryIDD = send_custom_mass_mail.apply_async(args = [mail._from,mail._group,mail._subject,mail._company,mail._body,file_path,mail._template], eta=etaTimezone)
        mail.celeryID = celeryIDD.id
        mail.status = celeryIDD.status
        mail.save()
        return data
