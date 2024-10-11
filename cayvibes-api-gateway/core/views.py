<<<<<<< HEAD
import json

from django.core.serializers.json import DjangoJSONEncoder

from core.producer import publish
from core.serializers import (
    LoginSerializer,
    LogoutSerializer,
    OtpVerificationSerializer,
    CelebritySerializer,
    FanSerializer,
    NgoSerializer
)
=======

from core.serializers import UserSerializer, LoginSerializer, OtpVerificationSerializer
>>>>>>> d0568b6 (adding files)
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from core.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from core.utils import send_code_to_user, validate_otp
<<<<<<< HEAD
from rest_framework_simplejwt.tokens import RefreshToken
=======


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_data = request.data
        serializer = self.get_serializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_code_to_user(user.email)
            return Response({
                'data': serializer.data, 
                'message': f'Hi {user.full_name}, thanks for signing up to this app'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> d0568b6 (adding files)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
<<<<<<< HEAD
=======
    permission_classes = [AllowAny]
>>>>>>> d0568b6 (adding files)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OTPVerificationAPIView(APIView):
<<<<<<< HEAD
=======
    permission_classes = [AllowAny]
>>>>>>> d0568b6 (adding files)
    serializer_class = OtpVerificationSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp_code = request.data.get('otp_code')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if validate_otp(user, otp_code):
            user.is_verified = True
            user.save()
            return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid or expired OTP.'}, status=status.HTTP_400_BAD_REQUEST)

<<<<<<< HEAD

class LogoutAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh']
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Add the token to the blacklist
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_205_RESET_CONTENT)

        #json.dumps(validated_data)


class CelebrityAPIView(APIView):
    serializer_class = CelebritySerializer

    def post(self, request):
        # Validate request data using serializer
        serializer = CelebritySerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.create(
                email=validated_data['email'],
                full_name=validated_data['stage_name'],
                stage_name=validated_data['stage_name'],
                terms=validated_data['terms'],
                country=validated_data['country'],
            )

            user.set_password(validated_data['password'])
            user.save()

            celebrity_data = {**validated_data, 'userId': user.id}

            # Publish message to RabbitMQ
            try:
                publish(f"{validated_data['account_type']}", 'celebrity.created', json.dumps(celebrity_data, cls=DjangoJSONEncoder))
            except Exception as e:
                # Handle RabbitMQ publishing errors
                return Response({"detail": f"Failed to publish message to RabbitMQ: {e}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"message": "Please wait for otp to complete registration"}, status=status.HTTP_200_OK)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FanAPIView(APIView):
    serializer_class = FanSerializer

    def post(self, request):
        # Validate request data using serializer
        serializer = FanSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.create(
                email=validated_data['email'],
                full_name=validated_data['legal_name'],
                terms=validated_data['terms'],
                country=validated_data['country'],
            )

            celebrity_data = {
                **validated_data,
                'userId': user.id
            }
            # Publish message to RabbitMQ
            try:
                publish(f"{validated_data['account_type']}", 'fan.created', celebrity_data)
            except Exception as e:
                # Handle RabbitMQ publishing errors
                return Response({"detail": f"Failed to publish message to RabbitMQ: {e}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NgoAPIView(APIView):
    serializer_class = NgoSerializer

    def post(self, request):
        # Validate request data using serializer
        serializer = NgoSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User.objects.create(
                email=validated_data['email'],
                full_name=validated_data['registration_name'],
                phone=validated_data['phone'],
                terms=validated_data['terms'],
                country=validated_data['country'],
            )

            celebrity_data = {
                **validated_data,
                'userId': user.id
            }
            # Publish message to RabbitMQ
            try:
                publish(f"{validated_data['account_type']}", 'ngo.created', celebrity_data)
            except Exception as e:
                # Handle RabbitMQ publishing errors
                return Response({"detail": f"Failed to publish message to RabbitMQ: {e}"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
    
>>>>>>> d0568b6 (adding files)
