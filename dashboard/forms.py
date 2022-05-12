from django import forms 
from .models import Mascotas, Adopciones,Madopcion

class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        
        fields = ['Adoptante','Nombre', 'Especie', 'Raza', 'Alimentacion', 'Edad', 'Fecha', 'Sexo', 'Enfermedad']

class AdopcionesForm(forms.ModelForm):
    class Meta:
        model = Adopciones
        
        fields = ['Nombre', 'Apellidos', 'Edad', 'Correo', 'Telefono','Domicilio', 'Numero_de_mascotas', 'Razones']

class MadopcionForm(forms.ModelForm):
    class Meta:
        model = Madopcion
        
        fields = ['Nombre', 'Raza', 'Especie', 'Sexo', ' imagen']
