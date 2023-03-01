from rest_framework import serializers


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'https: // www.youtube.com' not in value.get('link_video'):
            raise serializers.ValidationError('Поле не должно содержать ссылок на сторонние ресурсы,кроме youtube.com')

    # https: // www.youtube.com
