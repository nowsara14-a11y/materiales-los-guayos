from django.shortcuts import render
from .models import Producto

def home(request):
    # Consulta todos los productos disponibles en la base de datos
    productos = Producto.objects.filter(disponible=True)
    
    # Se los pasa a la plantilla index.html
    return render(request, 'index.html', {'productos': productos})