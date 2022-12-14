# Generated by Django 3.2.9 on 2022-08-01 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0023_auto_20220801_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snakehighscore',
            options={'get_latest_by': ['next_allowed_update', 'time_ten_minutes']},
        ),
        migrations.AlterField(
            model_name='snakehighscore',
            name='next_allowed_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 1, 12, 58, 15, 54960), null=True),
        ),
        migrations.AlterField(
            model_name='snakehighscore',
            name='time_ten_minutes',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 1, 13, 8, 15, 54989), null=True),
        ),
    ]
