from django.db import models


class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    categoria = models.CharField('Categoria', max_length=200)
    descripcion = models.TextField('Descripcion')
    precio = models.IntegerField('Precio')

    def __str__(self):
        return '{0}'.format(self.nombre)
