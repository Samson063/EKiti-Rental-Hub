from rest_framework import serializers
from .models import User
from rest_framework.serializers import StringRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from datetime import datetime, timedelta
    
CHOICES = [('student', 'Student'), ('agent', 'Agent'), ('tenant', 'Tenant')];
STATUS = [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')];
GENDER = [('male', 'male'), ('female', 'female')]

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=30, default='',required=False)
    last_name = serializers.CharField(max_length=30, default='',required=False)
    gender = serializers.ChoiceField(choices=GENDER)
    user_type = serializers.ChoiceField(choices=CHOICES)
    occupation = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=50)
    marital_status = serializers.ChoiceField(choices=STATUS)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

class PasswordResetVerifiedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=128)

class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)

class EmailChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

class EmailChangeVerifySerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'phone', 'user_type', 'address']
        extra_kwargs = {'password': {'write_only': True}}

class SettingsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    user_type = serializers.ChoiceField(required=False, choices=CHOICES)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'phone', 'user_type', 'address']
        extra_kwargs = {
            'email': {'read_only': True},
            'username': {'read_only': True},
            'user_type': {'read_only': True}
        }