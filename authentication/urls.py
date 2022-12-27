from django.urls import path
from . views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', TokenRefreshView.as_view()),
    path('otp/' ,OTP_send.as_view()),
    path('otp_verify/', Verify_OTP.as_view()),
    path('registration/' ,New_user_registration.as_view()),
    path('login/', Login.as_view()),
    path('otp_reset_password/', Reset_Password_OTP_View.as_view()),
    path('enter_new_password/', Password_Change_View.as_view()),
]
