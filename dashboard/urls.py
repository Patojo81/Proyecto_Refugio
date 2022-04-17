from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
    path('adopciones/', views.adopciones, name = 'dashboard-adopciones'),
    path('adopciones/delete/<int:pk>/', views.adopciones_delete, name = 'dashboard-adopciones-delete'),
    path('adopciones/update/<int:pk>/', views.adopciones_update, name = 'dashboard-adopciones-update'),
    path('mascotas/', views.mascotas, name = 'dashboard-mascotas'),
    path('agregar_mascotas/', views.agregar_mascotas, name = 'dashboard-agregar_mascotas'),
    path('agregar_mascotas/delete/<int:pk>/', views.agregar_mascotas_delete, name = 'dashboard-agregar_mascotas-delete'),
    path('agregar_mascotas/update/<int:pk>/', views.agregar_mascotas_update, name = 'dashboard-agregar_mascotas-update'),
    
    


]
