# Generated by Django 2.1.2 on 2018-10-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20181014_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生日'),
        ),
    ]