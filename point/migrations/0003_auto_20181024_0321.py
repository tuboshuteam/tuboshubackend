# Generated by Django 2.1.2 on 2018-10-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0002_auto_20181024_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='duration',
        ),
        migrations.AlterField(
            model_name='point',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='expend',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]
