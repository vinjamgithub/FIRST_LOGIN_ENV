# Generated by Django 4.1.3 on 2022-12-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='caps',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
