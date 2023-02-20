# Generated by Django 4.1.7 on 2023-02-20 06:11

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
                ('link_video', models.FileField(blank=True, null=True, upload_to='lessons_video/', verbose_name='видео')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('course_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='training.course', verbose_name='урок из курса')),
            ],
        ),
    ]