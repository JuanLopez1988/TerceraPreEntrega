from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    stock = models.FloatField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=8, decimal_places=2)
    precioFinal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.precioUnitario = self.producto.price
        self.precioFinal = self.precioUnitario * self.cantidad
        super().save(*args, **kwargs)
