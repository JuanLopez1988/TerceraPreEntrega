from django.shortcuts import render
from .models import Cliente
from .forms import clientesSignUp

# Create your views here.

def clientes(request):
    if request.method == 'POST':
        forms = clientesSignUp(request.POST)
        if forms.is_valid():
            data = forms.cleaned_data
            user = Cliente(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])
            user.save()
        return render(request, "AppTemplates/inicio.html")
    else:
        form = clientesSignUp()
    return render(request, "clientes/clientes.html", {'form': form})

