from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

from django.db  import models


class Plato(models.Model):
    nombre = CharField(max_length=30)
    direccion = CharField(max_length=50)
    precio = IntegerField()
   