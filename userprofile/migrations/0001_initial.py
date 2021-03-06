# Generated by Django 2.1.2 on 2018-10-13 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('phone', models.TextField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('age', models.PositiveSmallIntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
