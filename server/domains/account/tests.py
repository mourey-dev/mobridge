from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class AccountManagerTest(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
            role=1,
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("password123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin = self.User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass", role=0
        )
        self.assertEqual(admin.email, "admin@example.com")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.check_password("adminpass"))

    def test_create_user_without_email_fails(self):
        with self.assertRaisesMessage(ValueError, "The email must be set"):
            self.User.objects.create_user(
                username="admin", email=None, password="password123", role=1
            )


class RegisterAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("register_api")

    def test_register_account(self):
        """
        Ensure to register new account.
        """
        data = {
            "email": "test123@example.com",
            "role": 1,
            "password": "Password123",
            "confirm_password": "Password123",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertIn("message", response.data)

    def test_register_password_mismatch(self):
        """
        Ensure registration fails when password and confirm_password do not match.
        """
        data = {
            "email": "test_mismatch@example.com",
            "role": 1,
            "password": "Password123",
            "confirm_password": "Password321",  # mismatch
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response.data)
        self.assertIn(
            "Confirm password is not the same as password.",
            response.data["non_field_errors"],
        )

    def test_register_password_too_short(self):
        """
        Password must be at least 8 characters.
        """
        data = {
            "email": "shortpass@example.com",
            "role": 1,
            "password": "Pass1",  # too short
            "confirm_password": "Pass1",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertContains(
            response, "at least 8 characters long", status_code=HTTP_400_BAD_REQUEST
        )

    def test_register_password_missing_requirements(self):
        """
        Password must contain at least:
        - one uppercase
        - one lowercase
        - one number
        """
        data = {
            "email": "nouppercase@example.com",
            "role": 1,
            "password": "password123",  # no uppercase
            "confirm_password": "password123",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertContains(
            response,
            "one lowercase letter, one number, and no special characters",
            status_code=HTTP_400_BAD_REQUEST,
        )

    def test_register_password_has_special_character(self):
        """
        Password must not contain special characters.
        Only uppercase, lowercase, and numbers allowed.
        """
        data = {
            "email": "specialchar@example.com",
            "role": 1,
            "password": "Password123!",  # contains "!" (not allowed)
            "confirm_password": "Password123!",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertContains(
            response,
            "one lowercase letter, one number, and no special characters",
            status_code=HTTP_400_BAD_REQUEST,
        )

    def test_register_no_email(self):
        """
        Registration should fail when email is missing.
        """
        data = {
            "role": 1,
            "password": "Password123",
            "confirm_password": "Password123",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    def test_register_no_role(self):
        """
        Registration should fail when role is missing.
        """
        data = {
            "email": "norole@example.com",
            "password": "Password123",
            "confirm_password": "Password123",
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertIn("role", response.data)
