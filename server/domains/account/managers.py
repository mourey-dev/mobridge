from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(
        self,
        email,
        password,
        **extra_fields,
    ):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        account = self.model(
            email=email,
            **extra_fields,
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(
        self,
        email,
        password,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
