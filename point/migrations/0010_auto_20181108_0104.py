# Generated by Django 2.1.2 on 2018-11-08 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0009_auto_20181107_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='travel_date_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
