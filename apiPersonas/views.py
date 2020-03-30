from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer


# lista basda en clase (lo que hace es crear una instancia del modelo Usuario)
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()  # Consulta para indicarle que datos traer
    serializer_class = PersonaSerializer  # le indica a Django Rest framework que modelo serializado se va utilizar


