from rest_framework import viewsets
from . import serializer
from . import models

class programadorViewSet(viewsets.ModelViewSet):
    queryset = models.programador.objects.all()
    serializer_class = serializer.programadorSerializer
