from django.urls import path
from . views import *

urlpatterns = [
    path('bulk_upload/', ImportStudentData.as_view())
]