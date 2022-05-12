from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
    path('adopciones/', views.adopciones, name = 'dashboard-adopciones'),
    path('agregar_adopcion/', views.agregar_adopcion, name = 'dashboard-agregar_adopcion'),
    path('adopciones/delete/<int:pk>/', views.adopciones_delete, name = 'dashboard-adopciones-delete'),
    path('adopciones/update/<int:pk>/', views.adopciones_update, name = 'dashboard-adopciones-update'),
    path('mascotas/', views.mascotas, name = 'dashboard-mascotas'),
    path('agregar_mascotas/', views.agregar_mascotas, name = 'dashboard-agregar_mascotas'),
    path('agregar_mascotas/delete/<int:pk>/', views.agregar_mascotas_delete, name = 'dashboard-agregar_mascotas-delete'),
    path('agregar_mascotas/update/<int:pk>/', views.agregar_mascotas_update, name = 'dashboard-agregar_mascotas-update'),

    path('adopciones/madopcion/delete/<int:pk>/', views.madopcion_delete, name = 'dashboard-madopcion-delete'),
    path('adopciones/madopcion/update/<int:pk>/', views.madopcion_update, name = 'dashboard-madopcion-update'),

    path('listar-mascotas/', views.Agregar_MascotasPdf.as_view(), name='mascotas_all'),
    path('listar-adopciones/', views.Agregar_AdopcionesPdf.as_view(), name='adopciones_all'),
    path('listar-usuarios/', views.Agregar_UsuariosPdf.as_view(), name='usuarios_all'),
    


]
