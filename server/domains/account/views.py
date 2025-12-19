from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_200_OK

from .serializers import RegisterAccountSerializer
from .serializers import EmailVerificationSerializer


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate Token & UID
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        verification_link = f"http://localhost:3000/verify-email/{uid}/{token}/"

        # Send Email
        subject = "Verify your account"
        message = f"Click the link to verify: {verification_link}"
        send_mail(subject, message, "noreply@myapp.com", [user.email])

        return Response({"message": "Register has been successfully"}, HTTP_201_CREATED)


class VerifyEmailAPIView:
    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        user.verified = True
        user.save()

        return Response({"message": "Account activated successfully"}, HTTP_200_OK)
