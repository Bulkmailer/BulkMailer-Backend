from urllib import request
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.task import *
from bulkmailer.celery import app
from mailer.serializers import *

from .models import *

# Create your views here.


# Create Group API
class CreateGroup(
    generics.CreateAPIView,
    generics.ListAPIView,
    generics.DestroyAPIView,
    generics.UpdateAPIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateGroupSerializer

    def get_object(self):
        return Groups.objects.get(id=self.request.data.get("id"))

    def get_queryset(self):
        return Groups.objects.filter(user=self.request.user.id)

    def post(self, request, *args, **kwargs):
        if (
            Groups.objects.filter(user=request.user.id)
            .filter(name=request.data.get("name"))
            .exists()
        ):
            return Response(
                {"msg": "Group with this name already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.POST._mutable = True
        request.data["user"] = request.user.id
        return self.create(request)

    def patch(self, request, *args, **kwargs):
        if (
            Groups.objects.get(id=self.request.data.get("id")).user.id
            != request.user.id
        ):
            return Response(
                {"msg": "permission denied"}, status=status.HTTP_400_BAD_REQUEST
            )
        if (
            Groups.objects.filter(user=request.user.id)
            .filter(name=request.data.get("name"))
            .exists()
        ):
            return Response(
                {"msg": "Group with this name already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        self.update(request, *args, **kwargs)
        return Response(
            {"status": "Group Updated Successfully."}, status=status.HTTP_200_OK
        )

    def delete(self, request):
        Groups.objects.get(id=request.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Bulk Upload of Data in Group
class BulkAddEmail(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_id = self.request.data.get("group_id")
        return Group_Details.objects.filter(group=group_id)

    @staticmethod
    def post(request, *args, **kwargs):
        dataRequest = request.data.get("data[]")
        group = Groups.objects.get(id=request.data.get("group"))
        for data in dataRequest:
            if not Group_Details.objects.filter(group=group.id).filter(
                email=data["email"]
            ).exists() and re.findall("@.", data["email"]):
                Group_Details.objects.create(
                    group=group,
                    email=data["email"],
                    name=data["name"],
                    gender=data["gender"],
                )

        return Response({"msg": "Data Imported Successfully"})


# View Group Details and Update API
class View_Group_data(
    generics.ListAPIView, generics.UpdateAPIView, generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewGroupDataSerializer

    def get_object(self):
        return Group_Details.objects.get(id=self.request.data.get("id"))

    def get(self, request):
        groupData = Group_Details.objects.filter(
            group=request.GET.get("group_id")
        ).order_by("-id")
        serializer = self.serializer_class(groupData, many=True)
        if not groupData.exists():
            return Response({"msg": "Nothing Found"}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        groupData = Group_Details.objects.get(id=self.request.data.get("id"))
        if (
            Group_Details.objects.filter(group=groupData.group)
            .filter(email=request.data.get("email"))
            .exists()
        ):
            return Response({"msg": "Email Already Exist in Group"})
        self.update(request, *args, **kwargs)
        return Response(
            {"status": "Profile Updated Successfully."}, status=status.HTTP_200_OK
        )

    def delete(self, request):
        Group_Details.objects.get(id=request.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ADD Contacts Manually API
class Add_Contact_Manually(generics.CreateAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddContactsManuallySerializer


# Send Mail Immediately API
class SendMassMail(
    generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = MassMailSerializer

    def get_object(self):
        return SentMail.objects.get(id=self.request.data.get("id"))

    def get(self, request):
        mailType = request.GET.get("schedulmail")
        data = SentMail.objects.filter(user=request.user.id)
        if mailType == "True":
            data = data.filter(scheduleMail=True).order_by("-id")
        else:
            data = data.filter(scheduleMail=False).order_by("-id")
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["user"] = request.user.id
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["user"] = request.user.id
        self.update(request, *args, **kwargs)
        return Response({"msg": "Mail has been updated"}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request):
        taskID = SentMail.objects.get(id=request.data.get("id")).celeryID
        app.control.revoke(taskID)
        SentMail.objects.get(id=request.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# File Upload For Mail API
class FileUploadModelView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer

    def get_queryset(self):
        return FileUploadForMail.objects.filter(mail=request.GET.get("mail"))

    def post(self, request, *args, **kwargs):
        if request.data["file"]:
            return super().post(request, *args, **kwargs)

    @staticmethod
    def delete(request):
        FileUploadForMail.objects.get(id=request.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ADD, DELETE, GET API for Mail Template
class TemplateView(
    generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = TemplateSerializer

    def get_queryset(self):
        return TemplateModel.objects.all().order_by("-id")

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def delete(self, request):
        TemplateModel.objects.get(id=request.data.get("id")).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
