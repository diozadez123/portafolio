
from apps.administracion.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        exclude = ('email',)

class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')
        

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['nombre']        

