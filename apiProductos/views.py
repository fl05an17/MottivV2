from django.shortcuts import render
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer


class ProductoList(viewsets.ModelViewSet):
    queryset = Producto.objects.all()  # Consulta para indicarle que datos traer
    serializer_class = ProductoSerializer  # le indica a Django Rest framework que modelo serializado se va utilizar

