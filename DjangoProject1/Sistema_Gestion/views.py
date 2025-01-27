from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import*
from .models import*


# Create your views here.
@login_required
def farmacia (request):
    return render(request, 'farmacia.html',)

@login_required
def facturas (request):
    facturas = Factura.objects.all()
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturas')
    else:
        form = FacturaForm()
    return render(request, 'facturas.html', {'facturas': facturas, 'form': form})

def inicio (request):
    return  render(request, 'farmacia.html')

@login_required
def menu (request):
    return render(request, 'menu.html')

def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render (request, 'sucursales.html', {'sucursales': sucursales})

def medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos.html', {'medicamentos': medicamentos,})

@login_required
def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventarios': inventarios})

