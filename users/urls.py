from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path

from users.views import UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView

urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view()),
    path('detail_user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('update_user/<int:pk>/', UserUpdateAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
