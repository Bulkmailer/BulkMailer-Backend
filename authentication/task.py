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
from django_celery_results.models import TaskResult
import re
from django.conf import settings


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
def send_custom_mass_mail(self,_from,_group,_subject,_company,_body,_template,mailID):

    
    groups = Group_Details.objects.filter(group=_group)
    appGmail = Gmail_APP_Model.objects.get(id=_from)
    datatuple = [{'name':group.name,'email':group.email} for group in groups]
    print(appGmail.email, appGmail.app_password)
    file_attached = FileUploadForMail.objects.filter(mail=mailID)
    print(file_attached)
    
    html = ''
    
    
    if _template is not None and _template != 'null':
        print(_template)
        html = str(Template.objects.get(id=_template).template)

    connections = get_connection(
        username=appGmail.email,
        
        password=appGmail.app_password,
    )
    messages = []
    
    by = appGmail.email
    
    if _company is not None:
        by = f'{_company} <{appGmail.email}>'
        
    print(_subject,_body)
    
    for recipient in datatuple:
         msg = EmailMultiAlternatives(_subject, _body,by, [recipient["email"]] , connection=connections)
         if _template is not None and _template != 'null':
             formatedhtml = html
             if re.findall('{name}',html):
                formatedhtml = html.format(name=recipient["name"])
             msg.attach_alternative(formatedhtml, "text/html")
        
         if file_attached.count() > 0:
            for file in file_attached:
                msg.attach_file(settings.MEDIA_ROOT + (f'/{file.file.name}'))
         messages.append(msg)
    return connections.send_messages(messages)


@shared_task(bind=True)
def status_update(self):
    pending_task_id = SentMail.objects.filter(status='PENDING')

    for i in pending_task_id:
        try :
            celery_id = TaskResult.objects.get(task_id=i.celeryID)
            i.status = celery_id.status
            print(celery_id.status)
            i.save()
            
        except:
            i.status = 'PENDING'
        
    return 'Done'
        
    

    
    
    