import hashlib
import json

import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from training.models import Course, Subscription
from users.models import User, Payment, PaymentLog
from users.permissions import UserUpdatePermissions
from users.serializator import UserSerializer, UserRetrieve


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieve


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserUpdatePermissions]


class PaymentApiView(APIView):
    """Подключить оплату через https://yoomoney.ru/"""

    def get(self, *args, **kwargs):
        course_pk = kwargs.get('pk')
        course_item = Course.objects.filter(pk=course_pk).first()
        context = {
            'receiver': settings.YOOMONEY_WALLET,
            'label': f'{course_item.title}',
            'sum': f'{course_item.price}'
        }

        return render(self.request, 'payment/payment_form.html', context)


class PaymentTinkoffApiView(APIView):

    def get(self, *args, **kwargs):
        course_pk = kwargs.get('pk')
        course_item = get_object_or_404(Course, pk=course_pk)

        payment = Payment.objects.create(user=self.request.user, pay_course=course_item.id, summ=course_item.price,
                                         payment_method=Payment.CASHLESS)
        user = User.objects.filter(email=self.request.user).first()

        data_for_request = {
            "TerminalKey": f'{settings.TERMINAL_KEY}',
            "Amount": course_item.price,
            "OrderId": course_item.pk,
            "Description": "Образовательный курс",
            "DATA": {
                "Phone": "+71234567890",
                "Email": user.email
            },
            "Receipt": {
                "Email": user.email,
                "Phone": "+79031234567",
                "EmailCompany": "b@test.ru",
                "Taxation": "osn",
                "Items": [
                    {
                        "Name": course_item.title,
                        "Price": course_item.price,
                        "Quantity": 1.00,
                        "Amount": course_item.price,
                        "PaymentMethod": "full_prepayment",
                        "PaymentObject": "commodity",
                        "Tax": "vat10",
                        "Ean13": "0123456789"
                    }
                ]
            }
        }

        response = requests.post('https://securepay.tinkoff.ru/v2/Init', json=data_for_request)

        subscription = Subscription.objects.create(user_id=self.request.user, course_id=course_item,
                                                   status=Subscription.STATUSE_ACTIVE)
        paymentlog = PaymentLog.objects.create(Description=data_for_request.get('Description'), **response.json())

        return Response(response.json())


class PaymentGetStateAPIView(APIView):

    def get(self, *args, **kwargs):
        payment_pk = kwargs.get('pk')
        payment_item = get_object_or_404(PaymentLog, pk=payment_pk)

        str_for_token = str(settings.TERMINAL_PASSWORD) + str(payment_item.PaymentId) + str(settings.TERMINAL_KEY)
        token = hashlib.sha256(str_for_token.encode())
        token = token.hexdigest()

        # tokentr = token[1]["Password"] + x["PaymentId"] + token[0]["TerminalKey"]

        data_for_request = {
            "TerminalKey": settings.TERMINAL_KEY,
            "PaymentId": payment_item.PaymentId,
            "Token": token
        }

        responce = requests.post('https://securepay.tinkoff.ru/v2/GetState', json=data_for_request)
        data_check = PaymentLog.objects.filter(check_status=None)
        print(data_check)
        return Response(responce.json())
