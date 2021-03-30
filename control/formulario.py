from django import forms
from django.forms import ModelForm
from .models import admin

class registroForm(ModelForm):
    class Meta:
    	model=admin
    	fields=['id', 'nombre', 'apellido','telefono','cedula']