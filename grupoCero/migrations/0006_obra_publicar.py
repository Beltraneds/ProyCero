# Generated by Django 3.2.4 on 2021-07-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoCero', '0005_categoria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='publicar',
            field=models.BooleanField(default=False),
        ),
    ]
