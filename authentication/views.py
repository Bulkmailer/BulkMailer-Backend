from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *


# API for sending OTP.
class OtpSend(generics.CreateAPIView):
    serializer_class = OTPSerializer


# OTP verification API.
class VerifyOTP(generics.CreateAPIView):
    serializer_class = OTPVerifySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Email Verified"}, status=status.HTTP_200_OK)


# Registration API
class NewUserRegistration(generics.CreateAPIView):
    serializer_class = NewUserSerializer


# Login API
class Login(generics.CreateAPIView):
    serializer_class = LoginSerializer


# Password OTP view


class ResetPasswordOtpView(generics.CreateAPIView):
    serializer_class = ResetPasswordViewOTPSerializer


# Reset Password API
class PasswordChangeView(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        email = self.request.data.get("email")
        user = NewUserResgistration.objects.get(email=email)
        return user

    def patch(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response(
            {"msg": "Password Change Successfullly"}, status=status.HTTP_200_OK
        )


# Gmail APP Password Add and get APIs
class AddGmailPass(
    generics.CreateAPIView, generics.ListAPIView, generics.UpdateAPIView
):
    serializer_class = GmailAPPModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return GmailAPPModel.objects.filter(user=self.request.user.id)

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["user"] = request.user.id
        return self.create(request)


# Gmail APP Password Update API
class UpdateAppPassword(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = UpdateAppPassword
    permission_classes = [IsAuthenticated]

    def get_object(self):
        email = self.request.data.get("email")
        app_pass = GmailAPPModel.objects.get(email=email)
        return app_pass

    def patch(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response(
            {"msg": "APP Password Change Successfullly"}, status=status.HTTP_200_OK
        )


# Profile Details Get and Update APIs


class ProfileDetails(generics.ListAPIView, mixins.UpdateModelMixin):
    serializer_class = ProfileDetailsUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = NewUserResgistration.objects.get(id=self.request.user.id)
        return user

    def get_queryset(self):
        return NewUserResgistration.objects.filter(id=self.request.user.id)

    def patch(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response(
            {"status": "Profile Updated Successfully."}, status=status.HTTP_200_OK
        )
