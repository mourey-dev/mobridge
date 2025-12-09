from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import RegisterAccountSerializer


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Register has been successfully"}, HTTP_201_CREATED)
