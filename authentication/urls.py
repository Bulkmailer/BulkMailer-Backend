from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path("token/", TokenRefreshView.as_view()),
    path("otp/", OTPSend.as_view()),
    path("otp_verify/", VerifyOTP.as_view()),
    path("registration/", NewUserRegistration.as_view()),
    path("login/", Login.as_view()),
    path("otp_reset_password/", ResetPasswordOTPView.as_view()),
    path("enter_new_password/", PasswordChangeView.as_view()),
    path("add_App_password/", AddGmailPass.as_view()),
    path("update_app_password/", UpdateAPPPassword.as_view()),
    path("get_profile_details/", ProfileDetails.as_view()),
]
