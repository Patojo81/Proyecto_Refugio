from django.contrib import admin
from .models import Adopciones, Mascotas
from django.contrib.auth.models import Group


admin.site.site_header = 'Refugio de Animales Admin'

class MascotasAdmin(admin.ModelAdmin):
    list_display =( 'id', 'Nombre', 'Fecha', 'Adoptante')

class AdopcionesAdmin(admin.ModelAdmin):
    list_display =( 'id', 'Nombre', 'Apellidos', 'Edad', 'Correo', 'Telefono','Domicilio', 'Numero_de_mascotas', 'Razones')



# Register your models here.
admin.site.register(Mascotas, MascotasAdmin)
admin.site.register(Adopciones,AdopcionesAdmin)
admin.site.unregister(Group)
