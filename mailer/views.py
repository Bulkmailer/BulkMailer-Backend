from rest_framework import generics,status,mixins
from mailer.serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from .models import *

# Create your views here.

# class CreateGroup(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = []

# class See(generics.ListAPIView):
    # serializer_class = CreateGroupSerializer
    
    # def get_queryset(self):
        # return Groups.objects.all()

# class ImportStudentData(generics.GenericAPIView):
    # parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]
    
    # def post(self, request, *args, **kwargs):
    #     group = request.data.get('group')
    #     file = request.FILES['excel']        
    #     df = pd.read_csv(file)
    #     print(df)
    #     student_resource = StudentResource()
    #     dataset = Dataset().load(df)
    #     result = student_resource.import_data(dataset,\
    #          dry_run=True, raise_errors = True)

    #     if not result.has_errors():
    #         result = student_resource.import_data(dataset, dry_run=False)
    #         return Response({"status": "Student Data Imported Successfully"})

    #     return Response({"status": "Not Imported Student Data"},\
    #              status=status.HTTP_400_BAD_REQUEST)
    # def post(self,request, *args, **kwargs):
        # group = request.data.get("group")
        # g = Groups.objects.get(id=group)
        # file = [{'email':'suhaillahmadd@gmail.com','name':'hala'},{'email':'ajhs@gaj.ca','name':'hola'}]
        # data = [Group_Details(group=g,email=e['email'],name=e['name']) for e in file]
        # Group_Details.objects.bulk_create(data)
        # return Response({'msg':'done'})
        
# class CreateGroup(generics.CreateAPIView,generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CreateGroupSerializer
    
#     def get_queryset(self):
#         return Groups.objects.all()
    
#     def post(self, request, *args, **kwargs):
#         request.POST._mutable = True
#         request.data['user'] = request.user.id
#         return self.create(request)
    
# class BulkAddEmail(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BulkDataADD
