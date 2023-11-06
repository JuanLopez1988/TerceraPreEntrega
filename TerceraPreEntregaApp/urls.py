from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='Inicio'),
    path('Venta/', views.Venta, name='Venta' ),
    path('DetalleVenta/', views.DetalleVenta_form, name='DetalleVenta'),
    path('Producto/', views.producto, name='Producto'),
    path('getProducto/', views.getProducto, name='getProducto'),
    path('getDetalleVenta/', views.getDetalleVenta, name='getDetalleVenta'),
    
    
]

