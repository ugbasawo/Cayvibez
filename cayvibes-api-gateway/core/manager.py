from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Please enter a valid email address'))

    def create_user(self, email, full_name, terms, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('An email address is requireed'))

        if not full_name:
            raise ValueError(_('Full name is requireed'))
        if not terms:
            raise ValueError(_('An email address is requireed'))

        user = self.model(email=email, full_name=full_name, terms=terms, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, terms, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is staff must be true for admin user'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is superuser must be true for admin user'))

        user = self.create_user(email, full_name, terms, password, **extra_fields)
        user.save(using=self._db)
        return user
