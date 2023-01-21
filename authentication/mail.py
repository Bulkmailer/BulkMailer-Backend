from django.core.mail import EmailMultiAlternatives
import random
from django.conf import settings
from django.utils import timezone
from . models import *
from django.utils import timezone

def send_otp(email):
    subject = "Here's your account verification mail"
    otp = random.randint(1001 , 9999)
    text  = f'Your One Time Password for verification on Bulk-Mailer is {otp}.\nValid for only 2 minutes.\n DO NOT SHARE IT WITH ANYBODY.\nSKILL EDGE'
    style = f'<p>Your One Time Password for verification on Bulk-Mailer is <strong style="font-size: 18px;">{otp}</strong>.</p><p>Valid for only 2 minutes.</p><p style="font-size: 18px;">DO NOT SHARE IT WITH ANYBODY.</p><div style="text-align:center; font-size:40px; color:grey; margin-top:20px;"><strong>BULK MAILER</strong></div>'
    email_by = settings.EMAIL_HOST
    otp_msg = EmailMultiAlternatives(subject, text,f'SDC <{email_by}>',[email])
    otp_msg.attach_alternative(style, "text/html")
    otp_msg.send()
    OTP_user = OTP.objects.get(email=email)
    OTP_user.otp = otp
    OTP_user.time_created = timezone.now()
    OTP_user.save()
