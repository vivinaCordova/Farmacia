from django.db import models
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your models here.

# Modelo base Persona
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo Cajero, que hereda de Persona
class Cajero(Persona):
    def generarFactura(self):
        pass

    def revisarInventario(self):
        pass

# Modelo Cliente, que también hereda de Persona
class Cliente(Persona):
    telefono = models.IntegerField()

    def realizarpago(self):
        pass

    def solicitarProducto(self):
        pass

# Modelo Factura
class Factura(models.Model):
    fecha = models.DateField()
    numero = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

# Modelo Medicamento
class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    precioIndividual = models.DecimalField(max_digits=10, decimal_places=2)
    dosis = models.DecimalField(max_digits=10, decimal_places=2)
    provedor = models.CharField(max_length=50, default='Proveedor predeterminado')
    categoria = models.CharField(max_length= 50)
    descripcion = models.TextField(null=True, blank=True)


# Modelo Sucursal
class Sucursal(models.Model):
    numero = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

# Modelo Inventario
class Inventario(models.Model):
    cantidad = models.IntegerField()
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='inventarios')
    sucursal = models.OneToOneField(Sucursal, on_delete=models.CASCADE, related_name="inventario")

    def verificarMedicamento(self):
        if self.cantidad == 0:
            return f"El medicamento '{self.medicamento.nombre}' no está disponible."
        else:
            return f"El medicamento '{self.medicamento.nombre}' está disponible con {self.cantidad} unidades."

class InventarioGeneral(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cantidad} de {self.medicamento} en {self.inventario.sucursal}"

