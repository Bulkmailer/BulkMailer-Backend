from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from . import models

# Register your models here.
admin.site.register(models.Groups)
admin.site.register(models.TemplateModel)
admin.site.register(models.SentMail)
admin.site.register(models.FileUploadForMail)


@admin.register(models.Group_Details)
class PersonAdmin(ImportExportModelAdmin):
    pass
