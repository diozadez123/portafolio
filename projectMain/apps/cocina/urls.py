
from django.urls import path, include , re_path
from apps.cocina import views

urlpatterns = [
   re_path(r'^$', views.cocina),
]