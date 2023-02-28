from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import UserUpdatePermissions
from users.serializator import UserSerializer, UserRetrieve


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieve


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserUpdatePermissions]
