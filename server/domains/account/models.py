from django.db import models
from django.contrib.auth import models as auth_models

from . import managers

from core.mixins.models import TimestampMixin


class Account(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    class Role(models.IntegerChoices):
        SUPERUSER = 0, "Admin"
        APPLICANT = 1, "Applicant"
        EMPLOYER = 2, "Employer"

    username = models.CharField(max_length=25, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.IntegerField(choices=Role.choices)

    # Manager
    objects = managers.AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("role",)


class Profile(TimestampMixin):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)

    birth_date = models.DateField()

    profile = models.ImageField(upload_to="static/user/profile/")

    bio = models.TextField(blank=True)
