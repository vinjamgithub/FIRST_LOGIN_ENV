# Generated by Django 4.1.3 on 2023-03-03 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapi', '0002_remove_empapi_email_remove_empapi_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empapi',
            name='confirmpassword',
        ),
    ]