from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from training.models import Course, Lesson, Subscription
from training.permissions import ModeratorPermissionCourse, ModeratorPermissionCourseCreate, \
    ModeratorPermissionLessonCreate, ModeratorPermissionLesson
from training.serializators import CourseSerializer, LessonSerializer, SubscriptionSerializer, CourseSerializerDetail
from training.tasks import check_update_course


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.all()
        return Course.objects.filter(user_create=self.request.user)


class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ModeratorPermissionCourseCreate]  # Запрещает менеджеру

    def perform_create(self, serializer):
        """ Переопределяем, чтобы сохранился user_create"""
        serializer.save(user_create=self.request.user)


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated,ModeratorPermissionCourse]  # Можно или менеджеру или создателю

    def perform_update(self, serializer):
        self.object = serializer.save()
        check_update_course.delay(self.object.pk)



class CourseRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CourseSerializerDetail
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermissionCourse]  # Можно или менеджеру или создателю


class CourseDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermissionCourse]  # Запрещает менеджеру


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Lesson.objects.all()
        return Lesson.objects.filter(user_create=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ModeratorPermissionLessonCreate]  # Запрещает менеджеру

    def perform_create(self, serializer):
        """ Переопределяем, чтобы сохранился user_create"""
        return serializer.save(user_create=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermissionLesson]  # Можно или менеджеру или создателю




class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermissionLesson]  # Можно или менеджеру или создателю


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ModeratorPermissionLesson]  # Запрещает менеджеру


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Переопределяем, чтобы изменить статус"""
        serializer.save(status=Subscription.STATUSE_ACTIVE)


class SubscriptionDeleteAPIView(generics.UpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status=Subscription.STATUSE_INACTIVE)
