# Generated by Django 3.2.9 on 2022-07-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0008_auto_20220717_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snakehighscore',
            name='profile',
        ),
        migrations.AddField(
            model_name='snakehighscore',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='snakehighscore',
            name='province',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
