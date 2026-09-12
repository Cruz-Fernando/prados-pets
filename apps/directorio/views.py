from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dueno

def registrar_dueno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Guardar en la base de datos usando nombre_completo
        Dueno.objects.create(
            nombre_completo=nombre,
            telefono=telefono,
            direccion=direccion
        )
        
        messages.success(request, '¡Dueño registrado con éxito!')
        return redirect('registrar_dueno')

    return render(request, 'directorio/dueno_form.html')