# Generated by Django 4.1.3 on 2022-12-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0008_rename_address1_userlogin_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]