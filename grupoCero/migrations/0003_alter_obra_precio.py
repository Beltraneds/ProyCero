# Generated by Django 3.2.4 on 2021-06-30 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoCero', '0002_obra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='precio',
            field=models.TextField(),
        ),
    ]
