from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Adopciones, Mascotas, Madopcion
from django.contrib.auth.models import Group


admin.site.site_header = 'Refugio de Animales Admin'
class MascotasAdmin(admin.ModelAdmin):
    list_display =( 'id', 'Nombre', 'Fecha', 'Adoptante')

class MadopcionesAdmin(admin.ModelAdmin):
    list_display =( 'id', 'Nombre', 'Raza', 'Sexo','Especie')

class AdopcionesAdmin(admin.ModelAdmin):
    list_display =( 'id', 'Nombre', 'Apellidos', 'Edad', 'Correo', 'Telefono','Domicilio', 'Numero_de_mascotas', 'Razones')
    




# Register your models here.
admin.site.register(Mascotas, MascotasAdmin)
admin.site.register(Madopcion,MadopcionesAdmin)
admin.site.register(Adopciones,AdopcionesAdmin)
admin.site.unregister(Group)
