<<<<<<< HEAD
from datetime import timezone, datetime

=======
>>>>>>> d0568b6 (adding files)
from rest_framework import serializers
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
<<<<<<< HEAD
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class CelebritySerializer(serializers.Serializer):
    stage_name = serializers.CharField(max_length=225)
    email = serializers.CharField(max_length=100)
    category = serializers.UUIDField(allow_null=True)
    instagram = serializers.URLField(max_length=100)
    twitter = serializers.URLField(max_length=100)
    facebook = serializers.URLField(max_length=100)
    date_of_birth = serializers.DateField()
    country = serializers.CharField(max_length=10)
    terms = serializers.BooleanField(default=True)
    facial_verification = serializers.BooleanField(write_only=True, allow_null=True)
    profile_picture = serializers.URLField(write_only=True, allow_null=True)
    account_type = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    def validate_date_of_birth(self, value):
        today = datetime.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError("Celebrity must be at least 18 years old")
        return value

    def validate_email(self, value):
        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("Celebrity is already registered")
        return value

    def validate_stage_name(self, value):
        user = User.objects.filter(stage_name=value).exists()
        if user:
            raise serializers.ValidationError("Stage name is already registered")
        return value


class NgoSerializer(serializers.Serializer):
    registration_name = serializers.CharField(max_length=225)
    email = serializers.CharField(max_length=100)
    phone = PhoneNumberField(max_length=100)
    website = serializers.URLField(max_length=100)
    registration_year = serializers.DateField(write_only=True)
    category = serializers.UUIDField()
    address = serializers.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    state = serializers.CharField(max_length=200)
    terms = serializers.BooleanField(default=True)
    cac = serializers.URLField(write_only=True, allow_null=True)
    account_type = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)


class FanSerializer(serializers.Serializer):
    legal_name = serializers.CharField(max_length=225)
    email = serializers.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    terms = serializers.BooleanField(default=True)
    account_type = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
=======


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'terms', 'password', 'confirm_password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove confirm_password from validated_data
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            terms=validated_data['terms']
        )
        
        return user
>>>>>>> d0568b6 (adding files)


class OtpVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=5)

<<<<<<< HEAD

=======
    
>>>>>>> d0568b6 (adding files)
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
<<<<<<< HEAD
        return user.tokens()

=======
        return user.tokens() 
    
>>>>>>> d0568b6 (adding files)
    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
<<<<<<< HEAD
            'email': user.email,
            'tokens': user.tokens()
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
=======
            'email': user.email,  
            'tokens': user.tokens()  
        }
>>>>>>> d0568b6 (adding files)
