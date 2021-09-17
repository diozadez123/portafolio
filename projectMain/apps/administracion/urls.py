
from django.urls import path, include , re_path
from apps.administracion.views import Admin_add, crud_view, add_user
from . import views
from .views import *




urlpatterns = [
    path('',crud_view ),
    
    path('user/', Admin_add),

    path('add_user/', views.registerUser, name="add_user"),   
    path('', views.index, name="index"),
]