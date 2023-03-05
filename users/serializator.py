from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        # exclude = ['user', ]
        fields = '__all__'

    def save(self, **kwargs):
        user = self.context['request'].user




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
        new_user = User.objects.create(email=validated_data['email'], password=make_password(validated_data['password']),)
        new_user.groups.add(1)# Добавляем в группу пользователей

        return new_user

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

