# Generated by Django 2.1.2 on 2018-10-13 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20181013_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avartar',
        ),
    ]
