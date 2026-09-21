from django.contrib import admin
from django.urls import path
from hardware.views import home  # Importas la vista que acabamos de crear
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Muestra la función home al entrar a '/'
]

# Configuración para servir las imágenes subidas en desarrollo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)