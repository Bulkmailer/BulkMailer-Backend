from django.conf import settings
import jwt
from rest_framework.exceptions import ValidationError
from rest_framework import authentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from . models import New_User_Resgistration

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None
        
        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user = New_User_Resgistration.objects.get(id=payload["user_id"])
            return (user, token)
            
        except jwt.ExpiredSignatureError as e:
            raise ValidationError({"error": ["Token has Expired"]})

        except jwt.exceptions.DecodeError as e:
            raise AuthenticationFailed('Invalid Token')