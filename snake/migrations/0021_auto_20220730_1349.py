# Generated by Django 3.2.9 on 2022-07-30 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0020_alter_snakehighscore_next_allowed_update'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snakehighscore',
            options={'get_latest_by': ['next_allowed_update']},
        ),
        migrations.AlterField(
            model_name='snakehighscore',
            name='next_allowed_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 30, 7, 49, 33, 68947)),
        ),
    ]
