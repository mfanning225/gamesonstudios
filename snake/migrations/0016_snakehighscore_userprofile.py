# Generated by Django 3.2.9 on 2022-07-28 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20220725_1352'),
        ('snake', '0015_remove_snakehighscore_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snakehighscore',
            name='userProfile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]