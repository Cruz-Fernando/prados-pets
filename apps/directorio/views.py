from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Dueno

def registrar_dueno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        try:
            # Guardar en la base de datos
            Dueno.objects.create(
                nombre_completo=nombre,
                telefono=telefono,
                direccion=direccion
            )
            messages.success(request, '¡Dueño registrado con éxito!')
            return redirect('registrar_dueno')

        except IntegrityError:
            # Notificación detallada de error solicitada por el líder
            messages.error(
                request, 
                f"Error [ERR-001]: El número de teléfono '{telefono}' ya está registrado. "
                "Causa: El teléfono debe ser único. Solución: Verifica el número o usa uno diferente."
            )

    return render(request, 'directorio/dueno_form.html')