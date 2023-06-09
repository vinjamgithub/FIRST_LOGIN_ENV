# Generated by Django 4.1.3 on 2022-12-16 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='credentials',
            name='position',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='authentication.position'),
            preserve_default=False,
        ),
    ]
