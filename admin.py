from django.contrib import admin
from .models import Producto, Banner, Categoria, Pedido

# Personalización del encabezado y títulos del Admin
admin.site.site_header = "Materiales Los Guayos — Panel de Control"
admin.site.site_title = "Ferretería Admin"
admin.site.index_title = "Gestión de Inventario y Ventas"


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla principal
    list_display = ('nombre', 'precio_usd', 'stock', 'estado_stock', 'categoria')
    
    # Filtros laterales rápidos
    list_filter = ('categoria', 'stock')
    
    # Buscador por nombre de herramienta/material
    search_fields = ('nombre', 'descripcion')
    
    # Permite editar el stock directamente desde la lista sin entrar al producto
    list_editable = ('stock', 'precio_usd')
    
    # Paginación
    list_per_page = 20

    # Método para mostrar alertas visuales de stock
    def estado_stock(self, obj):
        if obj.stock == 0:
            return "❌ Agotado"
        elif obj.stock <= 10:
            return f"⚠️ Poco Stock ({obj.stock})"
        return "✅ Disponible"
    
    estado_stock.short_description = "Estatus"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo', 'orden')
    list_editable = ('activo', 'orden')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'monto_total', 'metodo_pago', 'estado', 'fecha')
    list_filter = ('estado', 'metodo_pago', 'fecha')
    search_fields = ('cliente_nombre', 'cedula_rif', 'telefono')