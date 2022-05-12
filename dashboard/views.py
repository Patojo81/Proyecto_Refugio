from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from dashboard.utils import render_to_pdf
from .models import Mascotas, Adopciones,Madopcion
from .forms import MascotasForm, AdopcionesForm,MadopcionForm
from django.views.generic import View
from .utils import render_to_pdf
from django.contrib.auth.models import User


# Create your views here.
from django.http import JsonResponse

def lockout(request, credentials, *args, **kwargs):
    return JsonResponse({"status": "Su cuenta se ha bloqueado debido al numero de intentos fallidos. Contactar con un administrador para el desbloqueo de la misma."}, status=403)

def index(request):
    current_user = request.user
   
    nuser = current_user.username
   
    context={
        'nuser': nuser,
        }
    return render(request, 'dashboard/index.html', context)
    



def adopciones(request):
    items2 = Madopcion.objects.all()
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
        'items2': items2,     
    }

    return render(request, 'dashboard/adopciones.html', context)



def agregar_adopcion(request):
    if request.method == 'POST':
        form = MadopcionForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('dashboard-adopciones')
    else: 
            form =MadopcionForm()
    context={
        
        'form' : form,    
    }

    return render(request, 'dashboard/agregar_adopcion.html', context)



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

def madopcion_delete (request,pk):
    item =Madopcion.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect ('dashboard-adopciones')
    return render(request, 'dashboard/madopcion_delete.html')

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

def madopcion_update (request, pk):
    item= Madopcion.objects.get(id=pk)
    if request.method== 'POST':
        form=MadopcionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-adopciones')
    else:
            form = MadopcionForm(instance=item)
    context={
        'form' : form,

    }
    return render(request, 'dashboard/madopcion_update.html',context)

class Agregar_MascotasPdf (View):
   
    def get ( self, request, *args, **kwargs):
         items = Mascotas.objects.all()
         data ={
            'items' : items

         }
         pdf = render_to_pdf ('dashboard/lista_mascotas.html', data)
         return HttpResponse(pdf, content_type='application/pdf')


class Agregar_AdopcionesPdf (View):
    
    def get ( self, request, *args, **kwargs):
         items = Adopciones.objects.all()
         data ={
            'items' : items

         }
         pdf = render_to_pdf ('dashboard/lista_adopciones.html', data)
         return HttpResponse(pdf, content_type='application/pdf')

class Agregar_UsuariosPdf(View):
    
    def get(self, request, *args, **kwargs):
        workers = User.objects.all()
        data = {
            'count': workers.count(),
            'workers': workers,
        }
        pdf = render_to_pdf('dashboard/lista_Usuarios.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

