import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hardware.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Escribe aquí directamente el usuario y la contraseña que vas a usar para entrar
USERNAME_ADMIN = "administracion"
EMAIL_ADMIN = "nowsara14@gmail.com"
PASSWORD_ADMIN = "sara,01122009."  # Reemplaza por la contraseña que tú quieras usar

if not User.objects.filter(username=USERNAME_ADMIN).exists():
    User.objects.create_superuser(username=USERNAME_ADMIN, email=EMAIL_ADMIN, password=PASSWORD_ADMIN)
    print(f"✅ Superusuario '{USERNAME_ADMIN}' creado exitosamente.")
else:
    # Si ya existe, le asigna la nueva contraseña
    u = User.objects.get(username=USERNAME_ADMIN)
    u.set_password(PASSWORD_ADMIN)
    u.is_staff = True
    u.is_superuser = True
    u.save()
    print(f"🔄 Contraseña del superusuario '{USERNAME_ADMIN}' actualizada a la nueva clave.")