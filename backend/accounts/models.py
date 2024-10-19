from django.db import models
from django.contrib.auth.models import  BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserType(models.IntegerChoices):
    patient = 1, "patient"
    admin = 2, "admin"
    superuser= 3, "superuser"


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)  # Pass extra_fields here
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault('type', UserType.superuser.value)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True,blank=False, max_length=100, verbose_name="username")
    email = models.EmailField(unique=True,blank=False, max_length=254, verbose_name="email")
    password = models.CharField(max_length=130, blank=False)
    is_superuser = models.BooleanField(default=False, verbose_name=_("superuser"))
    is_staff = models.BooleanField(default=False, verbose_name=_("staff"))
    is_active = models.BooleanField(default=True, verbose_name=_("active"))
    is_verified = models.BooleanField(default=True, verbose_name="verified")
    created = models.DateTimeField(auto_now_add=True, verbose_name="create date")
    updated = models.DateTimeField(auto_now=True, verbose_name="update date")
    type = models.IntegerField(
        choices=UserType.choices,
        default=UserType.patient.value,
        verbose_name="type"
    )

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email',]
    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    
    def __str__(self):
        return self.username