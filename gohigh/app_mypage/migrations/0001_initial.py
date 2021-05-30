# Generated by Django 3.2.3 on 2021-05-29 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_registration', '0003_auto_20210529_1857'),
        ('app_study', '0003_auto_20210530_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mine', to='app_registration.profile')),
                ('study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mine', to='app_study.study')),
            ],
        ),
    ]