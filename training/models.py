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
    price = models.FloatField(default=100, verbose_name='цена курса')


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
    link_video = models.CharField(max_length=250, verbose_name='видео', **NULLABLE)
    course_title = models.ForeignKey('training.Course', verbose_name='урок из курса', on_delete=models.SET_NULL,
                                     **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    """Подписки на обновления курса"""
    STATUSE_ACTIVE = 'active'
    STATUSE_INACTIVE = 'inactive'
    STATUSES = (
        ('active', 'Вы подписанны на курс'),
        ('inactive', 'Вы не подписаны на курс'),
    )

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                                **NULLABLE)
    course_id = models.ForeignKey('training.Course', verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)
    status = models.CharField(max_length=15, choices=STATUSES, verbose_name='статус подписки', default=STATUSE_INACTIVE)
