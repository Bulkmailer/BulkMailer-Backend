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
    template = models.TextField()
    
    def __str__(self):
        return self.template