from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from rest_framework import serializers

import re

from .models import Account


class RegisterAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            serializers.ValidationError("Please provide valid email address")

        return email

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        # Match password rules
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$"

        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email is already exist.")

        if not re.match(pattern, password):
            raise serializers.ValidationError(
                "Password must be at least 8 characters long, contain one uppercase letter, "
                "one lowercase letter, one number, and no special characters."
            )

        # Check confirm password
        if password != confirm_password:
            raise serializers.ValidationError(
                "Confirm password is not the same as password."
            )

        # Remove unecessary fields
        data.pop("confirm_password")

        return data

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user


class EmailVerificationSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    def validate(self, data):
        uid = data.get("uid")
        token = data.get("token")

        # Decode the UID
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            raise serializers.ValidationError({"uid": ["Invalid user ID"]})

        # Check the token
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError({"token": ["Invalid or expired token"]})

        data["user"] = user
        return data
