from dataclasses import field, fields
from re import template
from .models import *
from django.core.exceptions import ValidationError
from rest_framework import serializers
from authentication.task import *
import pytz
from datetime import datetime
from bulkmailer.celery import app
from bs4 import BeautifulSoup


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
        fields = ['id','user','_from','_group','_company','_body','_subject','_template','scheduleMail','_year','_month','_date','_hour','_minute','status','celeryID','title']
    
    def update(self, instance, data):
        mail = SentMail.objects.get(id=instance.id)
        if mail.celeryID is not None:
            app.control.revoke(mail.celeryID)


        instance = super(MassMailSerializer,self).update(instance, data)
        mail = SentMail.objects.get(id=instance.id)
        if mail.scheduleMail == True:
            asia_tz = pytz.timezone('Asia/kolkata')
            asia_dt = asia_tz.localize(datetime(data['_year'], data['_month'], data['_date'], data['_hour'], data['_minute']))
            etaTimezone = asia_dt.astimezone(pytz.UTC)
            celeryIDD = send_custom_mass_mail.apply_async(args = [mail._from,mail._group,mail._subject,mail._company,mail._body,mail._template,mail.id], eta=etaTimezone)
        else:
            celeryIDD = send_custom_mass_mail.apply_async(args = [mail._from,mail._group,mail._subject,mail._company,mail._body,mail._template,mail.id])
        mail.celeryID = celeryIDD.id
        mail.status = celeryIDD.status
        mail.save()
        return data
    
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadForMail
        fields = '__all__'
    
    def create(self, data):
        file_data = dict(self.initial_data)
        mail = SentMail.objects.get(id=data['mail'].id)
        if file_data is not None and isinstance(file_data, dict):
            files = [FileUploadForMail(mail=mail, file=file) for file in file_data['file']]
            FileUploadForMail.objects.bulk_create(files)
        return data

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
    
    def create(self,data):
        Template_object = Template.objects.create(**data)
        if Template_object.template is None:
            file = f"media/media/template/{data['html_file'].name}"
            HTMLFile = open(file, "r")
            index = HTMLFile.read()
            S = BeautifulSoup(index, 'lxml')
            print(S.body.prettify())
            Template_object.template = S.body.prettify()
            Template_object.save()
        return data