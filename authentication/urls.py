from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path("token/", TokenRefreshView.as_view()),
    path("otp/", OTP_send.as_view()),
    path("otp_verify/", Verify_OTP.as_view()),
    path("registration/", New_user_registration.as_view()),
    path("login/", Login.as_view()),
    path("otp_reset_password/", Reset_Password_OTP_View.as_view()),
    path("enter_new_password/", Password_Change_View.as_view()),
    path("add_App_password/", Add_Gmail_Pass.as_view()),
    path("update_app_password/", Update_APP_Password.as_view()),
    path("get_profile_details/", Profile_details.as_view()),
]
