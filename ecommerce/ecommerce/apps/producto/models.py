from django.db import models

# Create your models here.

class Producto(models.Model):
	nombre = models.CharField(max_length=40)
	precio = models.IntegerField()
	descripcion = models.TextField(null=True)
	fecha_venta = models.DateField(null=True)
	def __str__(self):
		return '{}'.format(self.nombre)
