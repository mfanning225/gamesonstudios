# Generated by Django 3.2.9 on 2022-07-29 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0018_remove_snakehighscore_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakehighscore',
            name='next_allowed_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 18, 5, 35, 56439)),
        ),
    ]