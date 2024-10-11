<<<<<<< HEAD
import json
import random
import logging
from uuid import UUID

from django.core.mail import EmailMessage
from django.conf import settings
from core.models import User, OneTimePassword
logger = logging.getLogger(__name__)
=======
import random
from django.core.mail import EmailMessage
from django.conf import settings
from core.models import User, OneTimePassword
from django.utils import timezone
>>>>>>> d0568b6 (adding files)


def generate_otp(length=5):
    """Generates a secure one-time password (OTP) of given length."""
    return ''.join(str(random.SystemRandom().randint(0, 9)) for _ in range(length))


def send_code_to_user(email):
    """Sends a one-time passcode to the user's email for verification."""
    subject = 'One-time passcode for Email verification'
    otp_code = generate_otp(length=5)
    print(otp_code)  # remove later

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        print(f"User with email {email} does not exist.")  # Logging
        return False

<<<<<<< HEAD
    current_site = 'CayVibes - Connecting fans and celebrity'
=======
    current_site = 'Cayvibes.com'
>>>>>>> d0568b6 (adding files)
    email_body = f'Hi {user.full_name},\n\nThanks for signing up on {current_site}. Please verify your email with the one-time passcode: {otp_code}'
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    send_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])

    try:
        send_email.send(fail_silently=False)
        return True
    except Exception as e:
        print(f"Failed to send email to {email}. Error: {e}")  # Logging
        return False


def validate_otp(user, otp_code):
    """Validates the OTP for a given user."""
<<<<<<< HEAD
    logger.info(f'Validating OTP for user {user.email}')
    
    try:
        otp_record = OneTimePassword.objects.get(user=user, code=otp_code)
        if otp_record.is_valid():
            logger.info(f'OTP for user {user.email} is valid.')
            return True
        else:
            logger.warning(f'OTP for user {user.email} has expired.')
            return False
    except OneTimePassword.DoesNotExist:
        logger.warning(f'Invalid OTP for user {user.email}.')
        return False
=======
    print('user ', user)
    print('code ', otp_code)
    try:
        otp_record = OneTimePassword.objects.get(user=user, code=otp_code)
        if otp_record.is_valid():
            return True
        else:
            print("OTP has expired.")  # Logging
            return False
    except OneTimePassword.DoesNotExist:
        print("Invalid OTP.")  # Logging
        return False
>>>>>>> d0568b6 (adding files)
