from django.db.models.fields import CharField, IntegerField 

from django.db  import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    stock = IntegerField()

