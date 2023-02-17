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


class Payment(models.Model):
    """ Платежи, поля:
    - пользователь
    - дата оплаты
    - оплаченный курс или урок
    - сумма оплаты
    - способ оплаты: наличные или перевод на счет
    """
    CASH = 'cash'
    CASHLESS = 'cashless'
    STATUS_PAY = (
        ('cash', 'наличные'),
        ('cashless', 'перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', **NULLABLE)
    date_pay = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты', **NULLABLE)
    pay_course = models.ForeignKey('training.Course',on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey('training.Lesson',on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    summ = models.FloatField(verbose_name='сумма оплаты', default=0)
    payment_method = models.CharField(choices=STATUS_PAY, default=CASH,verbose_name='способ оплаты:',max_length=15)
