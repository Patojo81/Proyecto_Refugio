from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mascotas, Adopciones
from .forms import MascotasForm, AdopcionesForm 

# Create your views here.

def index(request):
    current_user = request.user
   
    nuser = current_user.username
   
    context={
        'nuser': nuser,
        }
    return render(request, 'dashboard/index.html', context)
    



def adopciones(request):
    items = Adopciones.objects.all()
    if request.method == 'POST':
        form = AdopcionesForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('dashboard-adopciones')
    else: 
            form = AdopcionesForm()
    context={
        'items': items,
        'form' : form,
       
    }

    return render(request, 'dashboard/adopciones.html', context)

@login_required
def mascotas(request):
    return render(request, 'dashboard/mascotas.html')

@login_required
def agregar_mascotas(request):
    #items = Mascotas.objects.all()
    current_user = request.user
    lname = current_user.id
    if lname == 1 :
        items = Mascotas.objects.all()
    else:
        items = Mascotas.objects.raw('SELECT * FROM dashboard_mascotas WHERE "Adoptante_id" = %s', [lname])
    
    if request.method == 'POST':
        form = MascotasForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('dashboard-agregar_mascotas')
    else: 
            form = MascotasForm()
    context={
        'items': items,
        'form' : form,
    }

    return render(request, 'dashboard/agregar_mascotas.html', context)

def agregar_mascotas_delete (request, pk):
    item =Mascotas.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect ('dashboard-agregar_mascotas')
    return render(request, 'dashboard/agregar_mascotas_delete.html')


def adopciones_delete (request,pk):
    item =Adopciones.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect ('dashboard-adopciones')
    return render(request, 'dashboard/adopciones_delete.html')

def agregar_mascotas_update (request, pk):
    item= Mascotas.objects.get(id=pk)
    if request.method== 'POST':
        form=MascotasForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-agregar_mascotas')
    else:
            form = MascotasForm(instance=item)
    context={
        'form' : form,
 
    }
    return render(request, 'dashboard/agregar_mascotas_update.html', context )

def adopciones_update (request, pk):
    item= Adopciones.objects.get(id=pk)
    if request.method== 'POST':
        form=AdopcionesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-adopciones')
    else:
            form = AdopcionesForm(instance=item)
    context={
        'form' : form,

    }
    return render(request, 'dashboard/adopciones_update.html',context)