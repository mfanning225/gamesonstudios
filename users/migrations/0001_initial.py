# Generated by Django 3.2.9 on 2022-07-14 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(choices=[('CAN', 'Canada'), ('USA', 'United States')], default=None, max_length=50)),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('ON', 'Ontario')], default=None, max_length=50)),
                ('city', models.CharField(choices=[('CAL', 'Calgary'), ('VAN', 'Vancouver')], default=None, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
