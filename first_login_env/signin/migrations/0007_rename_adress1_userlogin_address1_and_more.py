# Generated by Django 4.1.3 on 2022-12-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0006_remove_userlogin_proofimg_userlogin_adress1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='adress1',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='userlogin',
            old_name='adress2',
            new_name='address2',
        ),
    ]
