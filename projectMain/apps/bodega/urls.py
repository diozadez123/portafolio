
from django.urls import path, include , re_path
from apps.bodega import views

urlpatterns = [
   re_path(r'^$', views.bodega),
]
