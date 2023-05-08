# Generated by Django 4.2.1 on 2023-05-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programador',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='programador',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='programador',
            name='nickname',
        ),
        migrations.AddField(
            model_name='programador',
            name='alta',
            field=models.CharField(default='2023-05-08 16:39:31.405361+00:00', max_length=20),
        ),
        migrations.AddField(
            model_name='programador',
            name='apellidos',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='programador',
            name='ciudad',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='programador',
            name='direccion',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='programador',
            name='historial_clinico',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='programador',
            name='ingreso',
            field=models.CharField(default='2023-05-08 16:39:31.405361+00:00', max_length=20),
        ),
        migrations.AddField(
            model_name='programador',
            name='telefono',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='programador',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
    ]