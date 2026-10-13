from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre



class pedido(models.Model):
    producto = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    total = models.IntegerField()

    @property
    def total_formatted(self):
        return f"${self.total:,.0f}".replace(",", ".")

    def __str__(self) -> str:
        return self.producto