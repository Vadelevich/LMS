# Generated by Django 4.1.7 on 2023-02-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('training', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='link_video',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='видео'),
        ),
    ]