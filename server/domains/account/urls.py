from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from .views import RegisterAPIView

urlpatterns = (
    path("login/", TokenObtainPairView.as_view(), name="login_api"),
    path("register/", RegisterAPIView.as_view(), name="register_api"),
)
