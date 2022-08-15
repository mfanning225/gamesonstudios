# Generated by Django 3.2.9 on 2022-07-14 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
        ('snake', '0004_snakehighscore_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snakehighscore',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]