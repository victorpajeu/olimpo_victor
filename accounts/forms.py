from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

#Qualque usuário pode enviar
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
#para ser criado com django admin
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','name','is_active','is_staf']
