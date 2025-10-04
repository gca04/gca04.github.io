from django.shortcuts import render, redirect
from django.db import models
from .models import Cliente, Mascota

def lista_clientes(request):
    if request.method == 'POST':
        if 'crear_cliente' in request.POST:
            rut = request.POST.get('rut')
            nom_ap = request.POST.get('nom_ap')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            # Create Cliente (idCliente must be unique, you can use max+1 or AutoField)
            max_id = Cliente.objects.aggregate(models.Max('idCliente'))['idCliente__max'] or 0
            Cliente.objects.create(
                idCliente=max_id + 1,
                Rut=rut,
                Nom_ap=nom_ap,
                Telefono=telefono,
                email=email
            )
            return redirect('lista_clientes')
        elif 'crear_mascota' in request.POST:
            nombre_mascota = request.POST.get('nombre_mascota')
            animal = request.POST.get('animal')
            raza = request.POST.get('raza')
            chip = request.POST.get('chip')
            id_cliente = request.POST.get('id_cliente')
            cliente = Cliente.objects.get(idCliente=id_cliente)
            Mascota.objects.create(
                NombreMascota=nombre_mascota,
                Animal=animal,
                Raza=raza,
                chip=chip,
                idCliente=cliente
            )
            return redirect('lista_clientes')
    clientes = Cliente.objects.all()
    mascotas = Mascota.objects.all()
    return render(request, 'home.html', {
        'clientes': clientes,
        'mascotas': mascotas
    })

def eliminar_cliente(request, idCliente):
    if request.method == 'POST':
        Cliente.objects.filter(idCliente=idCliente).delete()
    return redirect('lista_clientes')