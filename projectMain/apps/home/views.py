from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'admin_temp/login.html')

    return render(reverse_lazy('index'))
    
        

