from django.db import models
from authentication.models import *

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
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200, choices=GENDER, blank=False)
    
    def __str__(self):
        return str(self.name) + "-" + str(self.email)
