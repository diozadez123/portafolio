from apps.administracion import form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy

from apps.administracion.form import AdminForm

from apps.administracion.models import User
from .form import CustomUserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'base/index.html', {})


def administracion (request):
    return render(request, 'base/base.html')

def Admin_add(request):
    
    return render(request, 'admin_temp/admin_add.html',{'form':form})     

def add_user(request):
    name = request.POST.get('username','')
    passw = request.POST.get('password','')
    tipoUser = request.POST.get('tipouser','')
    User.objects.create(nombre=name,password=passw, tipoUsuario=tipoUser)
    return redirect('/')


def crud_view(request):
    return render(request, 'admin_temp/crud.html')    
    
def registerUser(request):
    data = {
        'form': CustomUserForm(),
        'profile': ProfileForm(),   
    }
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect(to='index')
        data['form']=form
        data['profile']=profile
    
    return render(request, 'admin_temp/register.html', data)



    

    






   


