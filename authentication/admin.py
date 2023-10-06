from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.OTP)
admin.site.register(models.NewUserRegistration)
admin.site.register(models.GmailAPPModel)
