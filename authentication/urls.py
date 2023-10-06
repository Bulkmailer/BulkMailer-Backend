from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path("token/", TokenRefreshView.as_view()),
    path("otp/", OtpSend.as_view()),
    path("otp_verify/", VerifyOTP.as_view()),
    path("registration/", NewUserRegistration.as_view()),
    path("login/", Login.as_view()),
    path("otp_reset_password/", ResetPasswordOtpView.as_view()),
    path("enter_new_password/", PasswordChangeView.as_view()),
    path("add_App_password/", AddGmailPass.as_view()),
    path("UpdateAppPassword/", UpdateAppPassword.as_view()),
    path("get_ProfileDetails/", ProfileDetails.as_view()),
]
