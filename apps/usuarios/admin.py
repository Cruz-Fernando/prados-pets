from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Rol, Usuario


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    model = Usuario
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Prados Pets", {"fields": ("id_rol", "nombre_completo", "telefono", "estado")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Prados Pets", {"fields": ("id_rol", "nombre_completo", "telefono", "estado")}),
    )
    list_display = ("username", "nombre_completo", "id_rol", "estado", "is_active")


admin.site.register(Rol)
