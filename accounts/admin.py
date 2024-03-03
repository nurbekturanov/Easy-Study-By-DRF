from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("is_teacher",)}),)
    add_fieldsets = UserAdmin.add_fieldsets +((None, {"fields": ("email",)}),)

admin.site.register(User, CustomUserAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)