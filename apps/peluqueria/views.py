from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CitaPeluqueria

def calcular_duracion_estimada(tamano, servicio):
    """Lógica para el Requerimiento Funcional RF25"""
    duracion_base = 30 # Minutos base para baño en perro pequeño

    # Adición por tamaño
    if tamano == 'MEDIANO':
        duracion_base += 15
    elif tamano == 'GRANDE':
        duracion_base += 30

    # Adición por tipo de servicio
    if servicio == 'CORTE':
        duracion_base += 30
    elif servicio == 'COMPLETO':
        duracion_base += 45

    return duracion_base

def agendar_peluqueria(request):
    if request.method == 'POST':
        nombre_mascota = request.POST.get('nombre_mascota')
        raza = request.POST.get('raza')
        tamano = request.POST.get('tamano')
        servicio = request.POST.get('servicio')
        fecha_hora = request.POST.get('fecha_hora')
        observaciones = request.POST.get('observaciones')

        # Cálculo automático de tiempo (RF25)
        duracion = calcular_duracion_estimada(tamano, servicio)

        try:
            CitaPeluqueria.objects.create(
                nombre_mascota=nombre_mascota,
                raza=raza,
                tamano=tamano,
                servicio=servicio,
                fecha_hora=fecha_hora,
                duracion_estimada_min=duracion,
                observaciones=observaciones
            )
            messages.success(request, f'Cita agendada con éxito. Tiempo estimado: {duracion} minutos.')
            return redirect('peluqueria:agendar')
        except Exception as e:
            messages.error(request, f'Error al agendar la cita: {e}')

    return render(request, 'peluqueria/agendar_peluqueria.html')