from django.contrib.auth.models import AbstractUser
from django.db import models


class Rol(models.Model):
    """Roles del sistema: administrador, veterinario, auxiliar, groomer, domiciliario."""

    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.nombre_rol


class Usuario(AbstractUser):
    """
    Usuario del sistema (personal de la clínica), extiende el modelo de auth
    de Django en vez de crear autenticación desde cero.

    Mapeo con el diagrama entidad-relación:
      - nombre_usuario -> username (heredado)
      - contrasena_hash -> password (heredado, Django lo hashea automáticamente)
      - correo -> email (heredado)
    """

    id_usuario = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(
        Rol, on_delete=models.PROTECT, related_name="usuarios", null=True, blank=True
    )
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True)
    estado = models.CharField(max_length=20, default="activo")
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombre_completo or self.username

    @property
    def es_administrador(self):
        """True si el usuario es superusuario o su rol asignado es 'administrador'."""
        if self.is_superuser:
            return True
        return bool(self.id_rol and self.id_rol.nombre_rol == "administrador")
