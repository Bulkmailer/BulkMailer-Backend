from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(models.Groups)
admin.site.register(models.Template)
admin.site.register(models.SentMail)
admin.site.register(models.FileUploadForMail)

@admin.register(models.Group_Details)
class PersonAdmin(ImportExportModelAdmin):
    pass