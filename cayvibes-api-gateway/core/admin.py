from django.contrib import admin
from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['email', 'is_verified', 'is_active','created_at', 'updated_at']
=======
    list_display = ['email', 'is_verified', 'is_staff', 'is_active','created_at', 'updated_at']
>>>>>>> d0568b6 (adding files)

