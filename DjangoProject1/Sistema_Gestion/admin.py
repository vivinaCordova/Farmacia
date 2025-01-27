from django.contrib import admin
from .models import (
    Factura, Persona, Cajero, Cliente, Sucursal, Inventario, Medicamento, InventarioGeneral
    )
# Register your models here.
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'identificacion')
    search_fields = ('nombre', 'apellido', 'identificacion')

# Personalización para el modelo Cajero
@admin.register(Cajero)
class CajeroAdmin(PersonaAdmin):
    pass

# Personalización para el modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(PersonaAdmin):
    list_display = ('nombre', 'apellido', 'identificacion', 'telefono')

# Personalización para el modelo Factura
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'numero', 'subtotal', 'impuestos', 'total')
    list_filter = ('fecha',)
    search_fields = ('numero',)

# Personalización para el modelo Medicamento
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'precioIndividual','provedor', 'dosis', 'categoria', 'descripcion')
    search_fields = ('nombre', 'codigo', 'provedor', 'categoria', 'descripcion')

    def mostrar_informacion(self, obj):
        return obj.mostrarInformacion()

    mostrar_informacion.short_description = 'Información del Medicamento'

# Personalización para el modelo Inventario
@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'medicamento',)
    list_filter = ('medicamento',)
    search_fields = ['nombre', 'codigo']

# Personalización para el modelo Sucursal
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'direccion',)
    search_fields = ('numero', 'direccion',)

@admin.register(InventarioGeneral)
class InventarioSucursalAdmin(admin.ModelAdmin):
    list_display = ("inventario", "medicamento", "cantidad")
    list_filter = ("inventario__sucursal", "medicamento")
    autocomplete_fields = ['inventario']


