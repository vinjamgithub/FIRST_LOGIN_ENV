# Generated by Django 4.1.3 on 2022-12-19 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_position_credentials_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentials',
            name='position',
        ),
        migrations.DeleteModel(
            name='position',
        ),
    ]
