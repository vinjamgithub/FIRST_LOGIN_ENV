# Generated by Django 4.1.3 on 2023-03-03 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empapi',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empapi',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='empapi',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='empapi',
            name='password',
        ),
    ]
