# Generated by Django 4.2.1 on 2023-05-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellidos', models.CharField(default='', max_length=100)),
                ('direccion', models.CharField(default='', max_length=150)),
                ('ciudad', models.CharField(default='', max_length=50)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('ingreso', models.DateTimeField()),
                ('alta', models.DateTimeField()),
                ('historial_clinico', models.TextField(default='')),
            ],
        ),
    ]
