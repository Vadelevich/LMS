from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """Модель для курсов поля :
        - название
        - превью (картинка)
        - описание
     """
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор курса', on_delete=models.CASCADE,
                                    **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='название курса', )
    image = models.ImageField(upload_to='course/', verbose_name='картинка для курсов', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class Lesson(models.Model):
    """Модель для урока, поля :
    - название
    - описание
    - превью (картинка)
    - ссылка на видео
    """
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор урока', on_delete=models.CASCADE,
                                    **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='Название урока', )
    description = models.TextField(verbose_name='описание урока', **NULLABLE)
    image = models.ImageField(upload_to='lesson/', verbose_name='картинка для урока', **NULLABLE)
    link_video = models.FileField(upload_to='lessons_video/', verbose_name='видео', **NULLABLE)
    course_title = models.ForeignKey('training.Course', verbose_name='урок из курса', on_delete=models.SET_NULL,
                                     **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)