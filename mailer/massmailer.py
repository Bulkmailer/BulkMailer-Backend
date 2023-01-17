from cgitb import html
from email import message
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from authentication.models import *

from django.core.mail.message import EmailMultiAlternatives
from django.core.mail import get_connection

from mailer.models import Group_Details

def send_custom_mass_mail(_from,_group,_company,_body):

    
    groups = Group_Details.objects.filter(group=_group)
    appGmail = Gmail_APP_Model.objects.get(id=_from)
    datatuple = [{'name':group.name,'email':group.email} for group in groups]

    
    
    html = '''
<body style="background-color:grey">
    <table align="center" border="0" cellpadding="0" cellspacing="0"
           width="550" bgcolor="white" style="border:2px solid black">
        <tbody>
            <tr>
                <td align="center">
                    <table align="center" border="0" cellpadding="0" 
                           cellspacing="0" class="col-550" width="550">
                        <tbody>
                            <tr>
                                <td align="center" style="background-color: #007AF1;
                                           height: 50px;">
  
                                    <a href="#" style="text-decoration: none;">
                                        <p style="color:white;
                                                  font-weight:bold;">
                                           Software Incubator {name}
                                        </p>
                                    </a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
            <tr style="height: 300px;">
                <td align="center" style="border: none;
                           border-bottom: 2px solid #007AF1; 
                           padding-right: 20px;padding-left:20px">
  
                    <p style="font-weight: bolder;font-size: 42px;
                              letter-spacing: 0.025em;
                              color:black;">
                        Hello!
                        <br> Check out our Bulk Maiker
                    </p>
                </td>
            </tr>
  
            <tr style="display: inline-block;">
                <td style="height: 150px;
                           padding: 20px;
                           border: none; 
                           border-bottom: 2px solid #007AF1;
                           background-color: white;">
                    
                    <h2 style="text-align: left;
                               align-items: center;">
                        Lorem Ipsum : A sjbs shaj to 
                      anbs sss Softkndslware sdkjnsk in 2022
                   </h2>
                    <p class="data" 
                       style="text-align: justify-all;
                              align-items: center; 
                              font-size: 15px;
                              padding-bottom: 12px;">
                        Lorem Ipsum….??? Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.…
                    </p>
                    <p>
                        <a href=
"https://www.silive.in/"
                           style="text-decoration: none; 
                                  color:black; 
                                  border: 2px solid #007AF1; 
                                  padding: 10px 30px;
                                  font-weight: bold;"> 
                           Read More 
                      </a>
                    </p>
                </td>
            </tr>
        </tbody>
    </table>
    <img src="https://drive.google.com/file/d/18yVMn5RXJLKfiMQOg-X7ZiXgKz_42d4N/view?usp=sharing">
    
</body>
'''
    
    
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



    
    
    