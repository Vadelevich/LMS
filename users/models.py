from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from training.models import NULLABLE

class CustomUserManager(UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    objects = CustomUserManager()

    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)
    token = models.CharField(verbose_name='Токен', max_length=35, **NULLABLE)
    token_expired = models.DateTimeField(verbose_name='Дата истечения токена', **NULLABLE)
    new_password = models.CharField(verbose_name="новый пароль", max_length=128, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


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



