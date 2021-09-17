from django.urls import path, include , re_path
from apps.proveedores import views

urlpatterns = [
   re_path(r'^$', views.proveedores),
]