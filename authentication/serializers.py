from rest_framework import serializers
from authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128,min_length=8,write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password", 'token']

        read_only_fields = ["token"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128,min_length=8,write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "password", "token"]

        read_only_fields = ["token"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email","is_active"]
