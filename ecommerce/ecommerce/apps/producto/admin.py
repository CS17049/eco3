from django.contrib import admin

# Register your models here.
from apps.producto.models import Producto
admin.site.register(Producto)
