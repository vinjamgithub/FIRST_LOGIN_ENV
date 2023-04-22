# Generated by Django 4.1.3 on 2022-12-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0003_userlogin_proofimg_userlogin_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='Confirmpassword',
            new_name='confirmpassword',
        ),
        migrations.RenameField(
            model_name='userlogin',
            old_name='Lastname',
            new_name='firs_tname',
        ),
        migrations.RenameField(
            model_name='userlogin',
            old_name='Email',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userlogin',
            old_name='Firstname',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='Password',
        ),
        migrations.AddField(
            model_name='userlogin',
            name='email',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
