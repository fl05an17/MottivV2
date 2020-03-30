from django.db import models


class Persona(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=200)

    # funcion crea vista por defecto para cada instacnia de modelo persona
    # Cadena para representar el objeto Usuario (en el sitio de Admin, etc.)
    def __str__(self):
        return '{0},{1}'.format(self.apellido, self.nombre)  # Se declara y formatea una cadena
