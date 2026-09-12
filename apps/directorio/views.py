from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Dueno


@login_required
def registrar_dueno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        direccion = request.POST.get('direccion', '').strip()

        try:
            Dueno.objects.create(
                nombre_completo=nombre,
                telefono=telefono,
                direccion=direccion,
            )
            messages.success(request, '¡Dueño registrado con éxito!')
            return redirect('registrar_dueno')

        except IntegrityError:
            messages.error(
                request,
                f"Error [ERR-001]: El número de teléfono '{telefono}' ya está registrado. "
                "Causa: el teléfono debe ser único. Solución: verifica el número o usa uno diferente."
            )
            # Conservamos lo escrito para no obligar a retipear todo
            return render(request, 'directorio/dueno_form.html', {
                'nombre': nombre, 'telefono': telefono, 'direccion': direccion,
            })

    return render(request, 'directorio/dueno_form.html')