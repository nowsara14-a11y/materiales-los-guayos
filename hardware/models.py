from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ($ USD)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad en Stock")
    
    # Campo para subir la imagen del producto (se guardará en la carpeta /media/productos/)
    imagen = models.ImageField(upload_to='productos/', verbose_name="Imagen del Producto", blank=True, null=True)
    
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible para venta?")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} - ${self.precio_usd}"