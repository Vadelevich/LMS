from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from training.models import Course, Lesson, Subscription
from training.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'title',
            'image',
            'description',
            'link_video',
        )
        validators = [LinkValidator(field='link_video')]


class CourseSerializer(serializers.ModelSerializer):
    # lesson_count = serializers.SerializerMethodField()

    # Для сериализатора для модели курса реализуйте поле вывода уроков.

    # lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = (
            'title',
            'image',
            'description',
            # 'lesson_count',
            # 'lesson',
        )

    # def get_lesson_count(self, instance):
    #     """ Для модели курса добавьте в сериализатор поле вывода количества уроков. """
    #     return instance.lesson_set.count()
    #
    # def create(self, validated_data):
    #     lesson_data = validated_data.pop('lesson_set')
    #     new_course = Course.objects.get_or_create(**validated_data)
    #     for item in lesson_data:
    #         lesson, created = Lesson.objects.get_or_create(course_title=new_course,**item)
    #         print(created)
    #     return new_course


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ['user_id', ]

    def create(self, validated_data):
        new_subscription = Subscription.objects.create(**validated_data)
        return new_subscription
