# Generated by Django 3.2.4 on 2021-07-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupoCero', '0006_obra_publicar'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='comentario',
            field=models.TextField(default='--', null=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='tecnica',
            field=models.CharField(max_length=60),
        ),
    ]
