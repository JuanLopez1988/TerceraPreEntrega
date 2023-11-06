from django.shortcuts import render, redirect
from TerceraPreEntregaPalazzoApp.models import Producto, DetalleVenta
from TerceraPreEntregaPalazzoApp.forms import ProductoForm, DetalleVentaForm
from django.contrib import messages

def inicio(request):
    return render(request, "AppTemplates/inicio.html")

def producto(request):
    if request.method == 'POST':
        miFormulario = ProductoForm(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            messages.success(request, "Producto registrado exitosamente") 
            return redirect('getProducto')

    miFormulario = ProductoForm()
    return render(request, 'AppTemplates/Producto.html', {'form': miFormulario})

def getProducto(request):
    productos = Producto.objects.all()
    return render(request, 'AppTemplates/getProducto.html', {'productos': productos})

def Venta(request):
    ventas = DetalleVenta.objects.all()
    return render(request, "AppTemplates/Venta.html", {'ventas': ventas})

def DetalleVenta_form(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getDetalleVenta')
    else:
        form = DetalleVentaForm()

    return render(request, 'AppTemplates/DetalleVenta.html', {'form': form})

def getDetalleVenta(request):
    detalles_venta = DetalleVenta.objects.all()
    return render(request, 'AppTemplates/getDetalleVenta.html', {'detalles_venta': detalles_venta})
