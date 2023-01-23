from django.urls import path
from . views import *

urlpatterns = [
    path('create_group/',CreateGroup.as_view()),
    path('bulk_add/', BulkAddEmail.as_view()),
    path('view_group_data/', View_Group_data.as_view()),
    path('add_manually/', Add_Contact_Manually.as_view()),
    path('send_mail/', SendMassMail.as_view()),
    path('file_upload/',FileUploadModelView.as_view()),
    path('template_view/',TemplateView.as_view())
]