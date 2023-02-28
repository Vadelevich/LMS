from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ['user', ]


class UserSerializer(serializers.ModelSerializer):
    # history = PaymentSerializer(source='payment_set',many=True,)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            # 'history',
        )

    def create(self, validated_data):
        """Переопределим, чтобы хешировался пароль"""
        return User.objects.create(email=validated_data['email'], password=make_password(validated_data['password']))

    def update(self, instance, validated_data):
        """ Изменим пароль """
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UserRetrieve(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'date_joined', 'is_staff')
