from rest_framework import serializers

from training.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'title',
            'image',
            'description',
            'link_video',
        )


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

    def get_lesson_count(self, instance):
        """ Для модели курса добавьте в сериализатор поле вывода количества уроков. """
        return instance.lesson_set.count()



