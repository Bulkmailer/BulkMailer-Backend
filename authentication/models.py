from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, user_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),user_name=user_name,name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, user_name, password,):
        user = self.create_user(
            email,
            password=password,
            name=name,
            user_name=user_name,
        )
        user.is_admin = True
        user.save()
        return user


class New_User_Resgistration(AbstractBaseUser):
   GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    
   email = models.EmailField(verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator()])
   name = models.CharField(max_length=150, default=None)
   user_name = models.CharField(max_length=150, blank=True, null=True, default=None, unique=True)
   gender = models.CharField(max_length=1, choices=GENDER, blank=False,default="M")
   mobile = models.BigIntegerField(blank=True)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)

   objects = MyUserManager()
    
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['name','user_name',]
   
    
   def __str__(self):
        return self.email
    




class OTP(models.Model):
     email = models.EmailField(verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator()])
     otp = models.CharField(max_length=4, blank=True, null=True)
     time = models.DateTimeField(default=timezone.now)
     
        
     def __str__(self):
         return self.email

