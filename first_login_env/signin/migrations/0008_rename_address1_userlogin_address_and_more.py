# Generated by Django 4.1.3 on 2022-12-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0007_rename_adress1_userlogin_address1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='userlogin',
            old_name='address2',
            new_name='secondaddress',
        ),
    ]