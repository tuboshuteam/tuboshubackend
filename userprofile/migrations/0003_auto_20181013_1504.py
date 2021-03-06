# Generated by Django 2.1.2 on 2018-10-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20181013_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
