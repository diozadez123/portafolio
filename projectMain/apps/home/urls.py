from django.urls import path, include , re_path
from apps.home.views import home, login


urlpatterns = [
    path('', home ),
    path('/', home ),

    path('login/', login),
    
]