from distutils.command import upload
from django.db import models
from authentication.models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field
# Create your models here.
class Groups(models.Model):
    user = models.ForeignKey(New_User_Resgistration,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Group_Details(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200, choices=GENDER, blank=False)
    
    def __str__(self):
        return str(self.name) + "-" + str(self.email)


class GroupResource(resources.ModelResource):
    group = Field(
        column_name='group',
        attribute='group',
        widget=ForeignKeyWidget(model=Groups))

    class Meta:
        model = Group_Details

class Template(models.Model):
    name = models.CharField(max_length=200)
    template = models.TextField()
    
    def __str__(self):
        return self.template

class SentMail(models.Model):
    user = models.ForeignKey(New_User_Resgistration, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    _from = models.CharField(max_length=200,null=True,blank=True)
    _group = models.CharField(max_length=200,null=True,blank=True)
    _company = models.CharField(max_length=200, null=True, blank=True)
    _body = models.CharField(max_length=200, null=True, blank=True)
    _subject = models.CharField(max_length=200,null=True,blank=True)
    _template = models.CharField(max_length=200, null=True, blank=True)
    _image = models.ImageField(upload_to="media",null=True, blank=True)
    scheduleMail = models.BooleanField(default=False)
    _year = models.IntegerField(null=True,blank=True)
    _month = models.IntegerField(null=True,blank=True)
    _date = models.IntegerField(null=True,blank=True)
    _hour = models.IntegerField(null=True,blank=True)
    _minute = models.IntegerField(null=True,blank=True)
    time = models.DateTimeField(auto_now=True)
    celeryID = models.CharField(max_length=200,null=True,blank=True) 
    status = models.CharField(max_length=200,default="PENDING")
    
    def __str__(self):
        return f'{self.user.name} -- {self._subject}'

class FileUploadForMail(models.Model):
    mail = models.ForeignKey(SentMail, on_delete=models.CASCADE)
    file = models.FileField(upload_to="media",null=True,blank=True)