# Generated by Django 3.2.4 on 2021-07-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoCero', '0007_auto_20210701_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='artista',
            field=models.CharField(default='--', max_length=60),
        ),
    ]
