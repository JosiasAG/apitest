from rest_framework import serializers
from . import models

class programadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.programador
        fields = '__all__'