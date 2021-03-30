from django.shortcuts import render 
from .models import admin
from .formulario import registroForm

def admins(request):
	data={
	    'form':registroForm()
	}
	if request.method=='POST':
	 formulario=registroForm(request.POST)
	 if formulario.is_valid():
	    formulario.save()
	    data['mensaje']="registro exitoso"
	return render(request, "save.html", data) 

def modificar(request,id):
    registro=admin.objects.get(id=id)
    data={
            'form':registroForm(instance=registro)
        }	   	
    if request.method=='POST':
            formulario=registroForm(data=request.POST, instance=registro)
            if formulario.is_valid():
                formulario.save()
                date['mensaje']="MODIFICADO CON EXITO"
                date['form']=formulario

    return render(request, "modificar.html", data) 

def eliminar_admins(request, id):
    admins=admin.objects.get(id=id)
    admins.delet()

    return render(request, "save.html")                       