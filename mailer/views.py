from rest_framework import generics,status,mixins
from rest_framework.response import Response
from mailer.serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from tablib import Dataset

# Create your views here.
        
class CreateGroup(generics.CreateAPIView,generics.ListAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = CreateGroupSerializer
        
        def get_queryset(self):
            return Groups.objects.filter(user=self.request.user.id)
        
        def post(self, request, *args, **kwargs):
            request.POST._mutable = True
            request.data['user'] = request.user.id
            return self.create(request)
        
class BulkAddEmail(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        group_id = self.request.data.get('group_id')
        return Group_Details.objects.filter(group=group_id)
    
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        group = request.data.get('group')
        groups = Groups.objects.get(id=group)
        df = pd.read_csv(file)
        df["group"] = int(groups.id)
        group_resouses =  GroupResource()
        dataset = Dataset().load(df)
        
        result = group_resouses.import_data(dataset,\
             dry_run=True, raise_errors = True)
        if not result.has_errors():
            result = group_resouses.import_data(dataset, dry_run=False)
            return Response({"msg": "Data Imported Successfully"})
        return Response({"msg": "Not Imported Data"},\
                 status=status.HTTP_400_BAD_REQUEST)
        
class View_Group_data(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewGroupDataSerializer
    def get_queryset(self):
        return Group_Details.objects.filter(group=self.request.data.get('group_id'))

class Add_Contact_Manually(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddContactsManuallySerializer
    
    