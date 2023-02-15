from django.urls import path
from rest_framework.routers import DefaultRouter

from training.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('list_lesson/',LessonListAPIView.as_view(),name='list_lesson'),
    path('create_lesson/',LessonCreateAPIView.as_view(),name='create_lesson'),
    path('update_lesson/<int:pk>/',LessonUpdateAPIView.as_view(),name='update_lesson'),
    path('destroy_lesson/<int:pk>/',LessonDestroyAPIView.as_view(),name='destroy_lesson'),
    path('retrieve_lesson/<int:pk>/',LessonRetrieveAPIView.as_view(),name='retrieve_lesson'),
              ] + router.urls
