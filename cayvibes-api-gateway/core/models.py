from django.utils import timezone
<<<<<<< HEAD
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from uuid import uuid4

from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from core.manager import UserManager

=======
from core.manager import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser,  PermissionsMixin)
from uuid import uuid4

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

>>>>>>> d0568b6 (adding files)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, unique=True, db_index=True)
<<<<<<< HEAD
    phone = PhoneNumberField(max_length=100)
    terms = models.BooleanField(default=True)
    stage_name = models.CharField(max_length=225, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    country = models.CharField(max_length=255, null=True, blank=True)
=======
    terms = models.BooleanField(default=True)
    stage_name = models.CharField(max_length=225)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
>>>>>>> d0568b6 (adding files)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
<<<<<<< HEAD
    REQUIRED_FIELDS = ['full_name', 'terms']
=======
    REQUIRED_FIELDS = [ 'full_name', 'terms', 'stage_name']
>>>>>>> d0568b6 (adding files)

    objects = UserManager()

    def __str__(self):
        return f'{self.email} {self.full_name}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_valid(self):
        return timezone.now() < self.created_at + timezone.timedelta(minutes=10)

    def __str__(self):
        return f'{self.user.full_name} passcode'
    
