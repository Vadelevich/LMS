from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.serializator import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

