from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from apps.directorio.models import Mascota
from .models import CitaPeluqueria
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime

def panel_peluqueria(request):
    """Renderiza el formulario de agendamiento de peluquería"""
    return render(request, 'peluqueria/agendar_peluqueria.html')


def buscar_mascota(request):
    """Buscador AJAX para filtrar mascotas ya registradas y mostrar su dueño"""
    q = request.GET.get('q', '').strip()
    resultados = []

    if len(q) >= 2:
        mascotas = Mascota.objects.select_related("id_dueno").filter(
            Q(nombre__icontains=q)
            | Q(id_dueno__nombre_completo__icontains=q)
            | Q(id_dueno__telefono__icontains=q)
            | Q(codigo_mascota__icontains=q)
        )[:10]

        for m in mascotas:
            resultados.append({
                'id': m.id_mascota,
                'nombre': m.nombre,
                'dueno': m.id_dueno.nombre_completo if m.id_dueno else 'Sin dueño',
                'raza': m.raza or 'No especificada',
                'tamano': getattr(m, 'tamano', 'PEQUENO')
            })

    return JsonResponse(resultados, safe=False)


def guardar_cita(request):
    """Procesa el formulario, guarda la cita y genera el PDF con todos los datos"""
    if request.method == 'POST':
        mascota_id = request.POST.get('mascota_id')
        servicio = request.POST.get('servicio')
        fecha_hora_str = request.POST.get('fecha_hora')
        
        # Convertir el string del input datetime-local a un objeto datetime de Python
        fecha_hora = None
        if fecha_hora_str:
            try:
                # El formato estándar que envían los inputs datetime-local es YYYY-MM-DDTHH:MM
                fecha_hora = datetime.strptime(fecha_hora_str, '%Y-%m-%dT%H:%M')
            except ValueError:
                try:
                    fecha_hora = datetime.strptime(fecha_hora_str, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    fecha_hora = None

        # Limpiar y obtener el precio ingresado en el formulario
        precio_raw = request.POST.get('precio', '$0')
        precio = precio_raw.strip()

        try:
            mascota = Mascota.objects.select_related("id_dueno").get(id_mascota=mascota_id)
        except Mascota.DoesNotExist:
            messages.error(request, 'Debe seleccionar una mascota válida del sistema.')
            return redirect('peluqueria:panel_peluqueria')

        nombre_mascota = mascota.nombre
        raza = mascota.raza or 'No especificada'
        tamano = getattr(mascota, 'tamano', 'MEDIANO')
        
        # Calcular duración estimada en minutos según el tamaño (RF25)
        duracion_min = 60
        if tamano == 'PEQUENO':
            duracion_min = 60
        elif tamano == 'MEDIANO':
            duracion_min = 90
        elif tamano == 'GRANDE':
            duracion_min = 120

        observaciones = request.POST.get('observaciones', '')

        # Crear la cita asegurando guardar la fecha convertida
        cita = CitaPeluqueria.objects.create(
            nombre_mascota=nombre_mascota,
            raza=raza,
            tamano=tamano,
            servicio=servicio,
            fecha_hora=fecha_hora,
            duracion_estimada_min=duracion_min,
            observaciones=observaciones
        )

        # Atributos auxiliares para el PDF
        cita.precio_formateado = precio
        cita.duracion_texto = f"{duracion_min // 60} hora(s)" if duracion_min == 60 else f"{duracion_min} minutos"

        # Configurar la respuesta PDF con xhtml2pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Comprobante_Spa_{mascota.nombre}.pdf"'

        template = get_template('peluqueria/pdf_cita.html')
        context = {'cita': cita, 'mascota': mascota}
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Hubo un error al generar el PDF del comprobante.', status=500)
            
        return response

    return redirect('peluqueria:panel_peluqueria')