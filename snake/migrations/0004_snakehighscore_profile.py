# Generated by Django 3.2.9 on 2022-07-14 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('snake', '0003_remove_snakehighscore_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakehighscore',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
