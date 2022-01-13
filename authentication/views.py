from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import response, status, permissions
from django.contrib.auth import authenticate

# Create your views here.


class AuthUserAPIView(GenericAPIView):

    permissions_classes = (permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return response.Response({'status': True, 'data': 'Hello World'})


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    authentication_classes = []

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
