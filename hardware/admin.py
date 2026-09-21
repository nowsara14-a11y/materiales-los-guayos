from django.contrib import admin
from .models import Producto  # Importa los modelos que tengas en tu models.py

# Personalización del título principal del Admin
admin.site.site_header = "Materiales Los Guayos — Panel de Control"
admin.site.site_title = "Ferretería Admin"
admin.site.index_title = "Gestión de Inventario y Ventas"


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_usd', 'stock', 'disponible')
    list_editable = ('precio_usd', 'stock', 'disponible')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('disponible',)

from django.contrib import admin
from .models import Producto  # Asegúrate de que 'Producto' exista en tu models.py
