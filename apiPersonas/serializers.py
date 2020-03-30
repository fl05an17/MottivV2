# convertir data a un tipo de archivo de intercambio de informacion (XML y JSON)

from rest_framework import serializers
from .models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre', 'apellido']