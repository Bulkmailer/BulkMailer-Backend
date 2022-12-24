from django.db import models
from authentication.models import *
from import_export import resources

# Create your models here.
class Groups(models.Model):
    user = models.ForeignKey(New_User_Resgistration,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Group_Details(models.Model):
    group = models.IntegerField()
    email = models.CharField(max_length=200)

class StudentResource(resources.ModelResource):

    class Meta:
        model = Group_Details
        import_id_fields = ["email","group"]
        skip_unchanged = True
        use_bulk = True