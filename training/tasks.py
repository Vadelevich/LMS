import hashlib

import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from training.models import Subscription
from users.models import PaymentLog


@shared_task
def check_update_course(course_pk):
    data_subscription = Subscription.objects.filter(course_id=course_pk)
    for item_subscription in data_subscription:
        send_mail(
            subject="Подписка на курс",
            message="Курс был обновлен! Взгляните на изменения! ",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[item_subscription.user_id],
            fail_silently=False

        )
        print(f'Письмо было отправлено {item_subscription.user_id}')

@shared_task
def check_status():
    data_check = PaymentLog.objects.filter(Status='NEW')
    print(data_check)
    if data_check.exists():
        for data_item in data_check:
            str_for_token = str(settings.TERMINAL_PASSWORD) + str(data_item.PaymentId) + str(settings.TERMINAL_KEY)
            token = hashlib.sha256(str_for_token.encode())
            token = token.hexdigest()

            data_for_request = {
                "TerminalKey": settings.TERMINAL_KEY,
                "PaymentId": data_item.PaymentId,
                "Token": token
            }
            responce = requests.post('https://securepay.tinkoff.ru/v2/GetState', json=data_for_request)
            print(responce.json())
            data_item.Status = responce.json()['Status']
            data_item.save()
            print("ok")

