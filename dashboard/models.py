from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
VAC = (

)
RAZA = (
    ('Hembra', 'Hembra'),
    ('Macho', 'Macho'),
)

class Madopcion (models.Model):
    Nombre = models.CharField(max_length=100, null=True)
    Sexo = models.CharField(max_length = 100, choices=RAZA, null=True)
    Especie = models.CharField(max_length=100, null=True)
    Raza = models.CharField(max_length=100, null=True)
    imagen = models.ImageField(default='avatar.jpg', upload_to='Mascotas_images')

class Mascotas(models.Model):
    
    Adoptante = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    Nombre = models.CharField(max_length=100, null=True)

    Especie = models.CharField(max_length=100, null=True)
    
    Raza = models.CharField(max_length=100, null=True)

    Alimentacion = models.CharField(max_length=100, null=True)

    Edad = models.PositiveIntegerField(null=True)

    Fecha = models.DateField(null=True)

    Sexo = models.CharField(max_length = 100, choices=RAZA, null=True)

    Enfermedad = models.CharField(max_length = 100, null=True)

    
    class Meta:
        
        verbose_name_plural ='Mascotas'

    def __str__(self):
        return f'{self.Nombre}-{self.Adoptante}'



        
class Adopciones(models.Model):
    Nombre  = models.CharField(max_length=100, null=True)
    Apellidos  = models.CharField(max_length=100, null=True)
    Edad  = models.PositiveIntegerField(null=True)
    Correo= models.CharField(max_length=100, null=True)
    Telefono = models.PositiveIntegerField(null=True)
    Domicilio = models.CharField(max_length=100, null=True)
    Numero_de_mascotas = models.PositiveIntegerField(null=True)
    Razones = models.CharField(max_length=100, null=True)






