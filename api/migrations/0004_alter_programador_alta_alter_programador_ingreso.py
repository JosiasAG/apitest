# Generated by Django 4.2.1 on 2023-05-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_programador_alta_alter_programador_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programador',
            name='alta',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='programador',
            name='ingreso',
            field=models.DateTimeField(),
        ),
    ]
