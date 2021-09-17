from django.db import models
from django.db.models.fields import CharField
from django.db  import models
from apps.bodega.models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


from django.contrib.auth.models import User

# Create your models here.

TIPO_USUARIO = (
('Admin', 'Admin'),
('Bodega', 'Codega'),
('Cocina', 'Cocina'),
)


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(default='Cocina',max_length=30,choices=TIPO_USUARIO)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre



""" class UserList(ListView):
    model = User  

class UserDetail(DetailView):
    model = User        

class UserCreation(CreateView):
    model = User
    success_url = reverse_lazy('user:list')
    fields = ['nombre', 'password', 'tipoUsuario']

class CourseUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('user:list')
    fields = ['nombre', 'password', 'tipoUsuario']    

class CourseDelete(DeleteView):
    model = User
    success_url = reverse_lazy('User:list') """




class Proveedor(models.Model):
    nombre = CharField(max_length=30)
    contacto = CharField(max_length=50)
    direccion = CharField(max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

