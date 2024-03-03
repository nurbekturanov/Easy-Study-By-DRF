from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PermissionsMixin):
    # TEACHER = "TEACHER"
    # STUDENT = "STUDENT"
    # USER = "USER"

    # ROLE_CHOICES = (
    #     (TEACHER, "Teacher"),
    #     (STUDENT, "Student"),
    #     (USER, "User"),
    # )

    # role = models.CharField(max_length=30, choices=ROLE_CHOICES, default=USER)
    email = models.EmailField(unique=True)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



# class CustomUserManager(BaseUserManager):
#     def create_superuser(self, email, user_name, password, **other_fields):

#         other_fields.setdefault('is_stuff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.'
#             )
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.'
#             )
        
#         return self.create_user(email, user_name, password, **other_fields)
    
#     def create_user(self, email, user_name, password, **other_fields):
#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name']

#     def __str__(self):
#         return self.user_name




   