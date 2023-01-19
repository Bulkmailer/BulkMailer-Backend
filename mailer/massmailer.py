from cgitb import html
from email import message
import imp
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from authentication.models import *

from django.core.mail.message import EmailMultiAlternatives
from django.core.mail import get_connection

from mailer.models import Group_Details
from .models import *

def send_custom_mass_mail(_from,_group,_company,_body):

    
    groups = Group_Details.objects.filter(group=_group)
    appGmail = Gmail_APP_Model.objects.get(id=_from)
    datatuple = [{'name':group.name,'email':group.email} for group in groups]

    
    
    html = str(Template.objects.get(id=1))
    print(appGmail.email, appGmail.app_password)
    
    connections = get_connection(
        username=appGmail.email,
        password=appGmail.app_password,
    )
    messages = []
    
    by = f'{_company} <{_from}>'
    
    for recipient in datatuple:
         msg = EmailMultiAlternatives("testing Email", "testing",by, [recipient["email"]] , connection=connections)
         formattedHtml = html.format(name=recipient["name"])
         msg.attach_alternative(formattedHtml, "text/html")
         messages.append(msg)
         

    print(messages)
    return connections.send_messages(messages)



    
    
    