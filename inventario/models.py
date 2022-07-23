from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
        
    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural= "Proveedores"


class Producto(models.Model):
    codigo = models.CharField(max_length=10, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

    def save(self, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural= "Productos"