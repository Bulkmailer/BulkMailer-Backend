from rest_framework import generics,status,mixins
from rest_framework.response import Response
from mailer.serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from .models import *

# Create your views here.
        
class CreateGroup(generics.CreateAPIView,generics.ListAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = CreateGroupSerializer
        
        def get_queryset(self):
            return Groups.objects.all()
        
        def post(self, request, *args, **kwargs):
            request.POST._mutable = True
            request.data['user'] = request.user.id
            return self.create(request)
        
class BulkAddEmail(generics.CreateAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = BulkDataADD
        
