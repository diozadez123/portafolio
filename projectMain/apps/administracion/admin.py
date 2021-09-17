from django.contrib import admin
from apps.administracion.models import User, Proveedor, Profile

# Register your models here.



""" admin.site.register(User) """
admin.site.register(Profile)
admin.site.register(Proveedor)