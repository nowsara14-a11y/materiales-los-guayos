from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta línea define la página de inicio en la raíz '/'
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]

# Configuración para ver imágenes cargadas en desarrollo/producción
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)