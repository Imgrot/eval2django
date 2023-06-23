from django.shortcuts import render, redirect
from eval2.forms import RegUser
from eval2.models import Participante

def main(request):
    return(render(request, 'main.html'))

def viewData(request):
    lista = Participante.objects.all()
    data = {'showUsers': lista}
    return render(request, 'showData.html', data)

def createData(request):
    formulario = RegUser()
    if request.method == 'POST':
        formulario = RegUser(request.POST)
        if formulario.is_valid():
            modelo = Participante()
            modelo.nombre = formulario.cleaned_data['nombre']
            modelo.telefono = formulario.cleaned_data['telefono']
            modelo.fecha = formulario.cleaned_data['fecha']
            modelo.empleador = formulario.cleaned_data['empleador']
            modelo.correo = formulario.cleaned_data['correo']
            modelo.profesion = formulario.cleaned_data['profesion']
            modelo.observaciones = formulario.cleaned_data['observaciones']
            modelo.save()
        return main(request)
    data = {'formulario' : formulario}
    return render(request, 'form.html', data)

def delData(request, id):
    proyecto = Participante.objects.get(id = id)
    proyecto.delete()
    return redirect('/list')

def modData(request, id):
    formulario = Participante.objects.get(id = id)
    form = RegUser(instance=formulario)

    if request.method == 'POST':
        form = RegUser(request.POST, instance=formulario)
        if form.is_valid():
            form.save()
        return main(request)
    data = {'formulario' : form}
    return render(request, 'form.html', data)