from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.



class Mesa(models.Model):
    nombre = CharField(max_length=30)
    tiop_mesa = CharField(max_length=50)
    pedido = models.CharField(max_length=50)
    total = IntegerField()
   