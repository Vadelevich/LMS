from django.urls import path

from users.views import UserRetrieveAPIView,UserCreateAPIView

urlpatterns = [
    path('create_user/',UserCreateAPIView.as_view()),
    path('detail_user/<int:pk>/',UserRetrieveAPIView.as_view()),
]