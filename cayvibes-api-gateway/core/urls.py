from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from core.views import (
    LoginAPIView,
    OTPVerificationAPIView,
    LogoutAPIView,
    CelebrityAPIView,
    FanAPIView,
    NgoAPIView
)

router = DefaultRouter()

urlpatterns = [
    re_path('celebrity/', CelebrityAPIView.as_view(), name='celebrity'),
    re_path('fans/', FanAPIView.as_view(), name='fans'),
    re_path('ngo/', NgoAPIView.as_view(), name='ngo'),
    re_path('login/', LoginAPIView.as_view(), name='login'),
    path('verify-otp/', OTPVerificationAPIView.as_view(), name='verify-otp'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls
=======
from core.views import UserViewSet, LoginAPIView, OTPVerificationAPIView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='register')

urlpatterns = [
    re_path('login/', LoginAPIView.as_view(), name='login'),
    path('verify-otp/', OTPVerificationAPIView.as_view(), name='verify-otp'),
]

urlpatterns += router.urls
>>>>>>> d0568b6 (adding files)
