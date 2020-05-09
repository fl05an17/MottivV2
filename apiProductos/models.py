from django.db import models


class Producto(models.Model):
    name = models.CharField('Nombre', max_length=100)
    description = models.TextField('Descripcion')
    price = models.IntegerField('Precio')
    imageUrl = models.TextField('Imagen')

    def __str__(self):
        return '{0}'.format(self.name)
