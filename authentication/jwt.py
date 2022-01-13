from math import radians
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from authentication.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)

        auth_token = auth_header.decode('utf-8').split(" ")

        if len(auth_token) != 2:
            raise AuthenticationFailed("Invalid token header")

        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            username = payload.get('username')

            user = User.objects.get(username=username)

            return (user, token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")
