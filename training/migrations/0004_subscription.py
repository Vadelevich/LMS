# Generated by Django 4.1.7 on 2023-02-27 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0003_alter_lesson_link_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=True, verbose_name='дата создания подписки')),
                ('status', models.CharField(
                    choices=[('active', 'Вы подписанны на курс'), ('inactive', 'Вы не подписаны на курс')],
                    default='inactive', max_length=15, verbose_name='статус подписки')),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                to='training.course', verbose_name='курс')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
