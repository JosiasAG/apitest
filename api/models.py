from django.db import models
import datetime
ahora = f'{datetime.datetime.day}/{datetime.datetime.month}/{datetime.datetime.year}'

class programador(models.Model):
    nombre= models.CharField(max_length=50, default = "")
    apellidos=models.CharField(max_length=100, default = "")
    direccion=models.CharField(max_length=150, default = "")
    ciudad=models.CharField(max_length=50, default = "")
    telefono=models.CharField(max_length=20, default = "")
    ingreso=models.DateTimeField()
    alta=models.DateTimeField()
    historial_clinico=models.TextField(default = "")
    
    def __str__(self):
        return self.nombre
