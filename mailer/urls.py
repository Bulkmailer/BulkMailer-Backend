from django.urls import path
from . views import *

urlpatterns = [
    path('create_group/',CreateGroup.as_view()),
    path('bulk_add/', BulkAddEmail.as_view())
]