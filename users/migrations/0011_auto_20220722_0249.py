# Generated by Django 3.2.9 on 2022-07-22 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220721_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.CreateModel(
            name='ProvinceState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='users.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='provinceState',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provinceState', to='users.provincestate'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='provinceState',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.provincestate'),
        ),
    ]