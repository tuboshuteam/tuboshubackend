# Generated by Django 2.1.2 on 2018-10-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_profile_avartar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
