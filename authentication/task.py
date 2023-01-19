from celery import shared_task
from django.core.mail import EmailMultiAlternatives
import random
from django.conf import settings
from django.utils import timezone
from . models import *
from django.utils import timezone
from django.core.mail.message import EmailMultiAlternatives
from django.core.mail import get_connection
from mailer.models import *
import re

from mailer.models import Group_Details
@shared_task(bind=True)
def send_otp(self,email):
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
    
    return 'Done'

@shared_task(bind=True)
def send_custom_mass_mail(self,_from,_group,_subject,_company,_body,file,_template):

    
    groups = Group_Details.objects.filter(group=_group)
    appGmail = Gmail_APP_Model.objects.get(id=_from)
    datatuple = [{'name':group.name,'email':group.email} for group in groups]
    print(appGmail.email, appGmail.app_password)
    
    html = ''
    
    if _template is not None:
        html = str(Template.objects.get(id=_template))

    connections = get_connection(
        username=appGmail.email,
        
        password=appGmail.app_password,
    )
    messages = []
    print('agaya')
    
    by = appGmail.email
    
    if _company is not None:
        print('skns')
        by = f'{_company} <{appGmail.email}>'
        
    print(_subject,_body)
    
    for recipient in datatuple:
         msg = EmailMultiAlternatives(_subject, _body,by, [recipient["email"]] , connection=connections)
         if _template is not None:
             if re.findall('{name}',html):
                print(re.findall('{name}',html))
                html = html.format(name=recipient["name"])
             msg.attach_alternative(html, "text/html")
         
         if file != 'None':
             msg.attach_file(file)
         
         messages.append(msg)
    print(messages)
    return connections.send_messages(messages)



    
    
    