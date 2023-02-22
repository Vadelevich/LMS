from django.urls import path
from rest_framework.routers import DefaultRouter

from training.views import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView, CourseListAPIView, CourseCreateAPIView, CourseUpdateAPIView, \
    CourseDestroyAPIView, CourseRetrieveAPIView

urlpatterns = [
    path('list_lesson/',LessonListAPIView.as_view(),name='list_lesson'),
    path('create_lesson/',LessonCreateAPIView.as_view(),name='create_lesson'),
    path('update_lesson/<int:pk>/',LessonUpdateAPIView.as_view(),name='update_lesson'),
    path('destroy_lesson/<int:pk>/',LessonDestroyAPIView.as_view(),name='destroy_lesson'),
    path('retrieve_lesson/<int:pk>/',LessonRetrieveAPIView.as_view(),name='retrieve_lesson'),
    path('list_course/',CourseListAPIView.as_view(),name='list_course'),
    path('create_course/',CourseCreateAPIView.as_view(),name='create_course'),
    path('update_course/<int:pk>/',CourseUpdateAPIView.as_view(),name='update_course'),
    path('destroy_course/<int:pk>/',CourseDestroyAPIView.as_view(),name='destroy_course'),
    path('retrieve_course/<int:pk>/',CourseRetrieveAPIView.as_view(),name='retrieve_course'),
              ]
