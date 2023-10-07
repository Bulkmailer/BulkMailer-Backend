from django.urls import path

from .views import *

urlpatterns = [
    path("create_group/", CreateGroup.as_view()),
    path("bulk_add/", BulkAddEmail.as_view()),
    path("ViewGroupData/", ViewGroupData.as_view()),
    path("add_manually/", AddContactManually.as_view()),
    path("send_mail/", SendMassMail.as_view()),
    path("file_upload/", FileUploadModelView.as_view()),
    path("template_view/", TemplateView.as_view()),
]
