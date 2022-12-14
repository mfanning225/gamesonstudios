# Generated by Django 3.2.9 on 2022-08-02 15:24

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0028_auto_20220802_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakehighscore',
            name='est_timezone',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='snakehighscore',
            name='next_allowed_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 2, 11, 24, 5, 600739), null=True),
        ),
        migrations.AlterField(
            model_name='snakehighscore',
            name='time_ten_minutes',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 2, 11, 25, 5, 600757), null=True),
        ),
    ]
