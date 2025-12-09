from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings

from rest_framework import serializers

import re


class RegisterAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    role = serializers.IntegerField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            serializers.ValidationError("Please provide valid email address")

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        # Match password rules
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$"

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

        return data

    def create(self, validated_data):
        User = settings.get_user_model()
        user = User.objects.create_user(**validated_data)
        return user
