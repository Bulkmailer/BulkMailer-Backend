from rest_framework import generics,status,mixins
from rest_framework.response import Response
from . models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
import pandas as pd
from tablib import Dataset
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
import csv

# Create your views here.


class ImportStudentData(generics.GenericAPIView):
    parser_classes = [MultiPartParser]
    
    def post(self, request, *args, **kwargs):
        group = request.data.get('group')
        file = request.FILES['excel']        
        df = pd.read_csv(file)
        print(df)
        student_resource = StudentResource()
        dataset = Dataset().load(df)
        result = student_resource.import_data(dataset,\
             dry_run=True, raise_errors = True)

        if not result.has_errors():
            result = student_resource.import_data(dataset, dry_run=False)
            return Response({"status": "Student Data Imported Successfully"})

        return Response({"status": "Not Imported Student Data"},\
                 status=status.HTTP_400_BAD_REQUEST)
