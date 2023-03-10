# Generated by Django 4.1.7 on 2023-03-01 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='картинка для курсов')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание курса')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание урока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='картинка для урока')),
                ('link_video', models.CharField(blank=True, max_length=250, null=True, verbose_name='видео')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Вы подписанны на курс'), ('inactive', 'Вы не подписаны на курс')], default='inactive', max_length=15, verbose_name='статус подписки')),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.course', verbose_name='курс')),
            ],
        ),
    ]
