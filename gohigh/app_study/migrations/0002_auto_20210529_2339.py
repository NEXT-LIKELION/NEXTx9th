# Generated by Django 3.2.3 on 2021-05-29 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_study', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penalty',
            name='study',
        ),
        migrations.RemoveField(
            model_name='study',
            name='absent_criterion',
        ),
        migrations.RemoveField(
            model_name='study',
            name='absent_penalty',
        ),
        migrations.RemoveField(
            model_name='study',
            name='categoty',
        ),
        migrations.RemoveField(
            model_name='study',
            name='is_online',
        ),
        migrations.RemoveField(
            model_name='study',
            name='late_criterion',
        ),
        migrations.RemoveField(
            model_name='study',
            name='late_penalty',
        ),
        migrations.RemoveField(
            model_name='study',
            name='mission_day',
        ),
        migrations.RemoveField(
            model_name='study',
            name='mission_time',
        ),
        migrations.AddField(
            model_name='study',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app_study.studycategory'),
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Penalty',
        ),
    ]
