# Generated by Django 3.2.3 on 2021-05-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mypage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mypage',
            name='Profile',
        ),
        migrations.AlterField(
            model_name='mypage',
            name='study',
            field=models.TextField(max_length=200),
        ),
    ]