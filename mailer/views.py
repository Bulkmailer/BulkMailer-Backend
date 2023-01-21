from ast import Delete
from rest_framework import generics,status,mixins
from rest_framework.response import Response
from mailer.serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from .models import *
from tablib import Dataset
import pytz
from authentication.task import *
from bulkmailer.celery import app

# Create your views here.
     
# Create Group API       
class CreateGroup(generics.CreateAPIView,generics.ListAPIView,generics.DestroyAPIView):
        permission_classes = [IsAuthenticated]
        serializer_class = CreateGroupSerializer
        
        def get_queryset(self):
            return Groups.objects.filter(user=self.request.user.id)
        
        def post(self, request, *args, **kwargs):
            request.POST._mutable = True
            request.data['user'] = request.user.id
            return self.create(request)
        def delete(self,request):
            Groups.objects.get(id=request.data.get('id')).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# Bulk Upload of Data in Group      
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

# View Group Details and Update API        
class View_Group_data(generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewGroupDataSerializer
    def get_queryset(self):
        return Group_Details.objects.filter(group=self.request.GET.get('group_id'))
    def patch(self, request, *args, **kwargs):
        self.update(request,*args, **kwargs)
        return Response({"status": "Profile Updated Successfully."}, status=status.HTTP_200_OK)
    def delete(self,request):
        Group_Details.objects.get(id=request.data.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ADD Contacts Manually API
class Add_Contact_Manually(generics.CreateAPIView,generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddContactsManuallySerializer

# Send Mail Immediately API
class SendMassMail(generics.CreateAPIView,generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MassMailSerializer
    
    def get_queryset(self):
        return SentMail.objects.filter(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['user'] = request.user.id
        return self.create(request)
    
#Scheduled Mail API
class SchedulingMailAPI(generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ScheduleMailSerializer
    
    def get_queryset(self):
        return SchedulingMail.objects.filter(user=self.request.user.id)
    
    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['user'] = request.user.id
        return self.create(request)
    def delete(self,request):
        scheduledMail = request.data.get('id')
        taskID = SchedulingMail.objects.get(id=scheduledMail).celeryID
        print(taskID)
        app.control.revoke(taskID)
        SchedulingMail.objects.get(id=scheduledMail).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
