from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from apps.directorio.models import Mascota

from .forms import CitaForm
from .models import Cita


@login_required
def agendar_cita(request):
    """HU06: Agendar consultas médicas."""
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                form.add_error(
                    None,
                    "Ya existe una cita para ese veterinario en esa fecha y hora.",
                )
            else:
                messages.success(request, "¡Cita agendada con éxito!")
                return redirect("agendamiento:agendar_cita")
    else:
        form = CitaForm()

    return render(request, "agendamiento/cita_form.html", {"form": form})


@login_required
def buscar_mascotas_ajax(request):
    """
    HU06-fix: Búsqueda de mascota por texto libre (AJAX).
    Busca por nombre de mascota, nombre del dueño, teléfono o código.
    Devuelve JSON con hasta 10 resultados.
    """
    q = request.GET.get("q", "").strip()
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
                "id": m.id_mascota,
                "nombre_mascota": m.nombre,
                "especie": m.get_especie_display(),
                "raza": m.raza or "-",
                "codigo": m.codigo_mascota,
                "dueno": m.id_dueno.nombre_completo,
                "telefono": m.id_dueno.telefono,
                "label": f"{m.nombre} ({m.codigo_mascota}) — {m.id_dueno.nombre_completo}",
            })

    return JsonResponse({"resultados": resultados})


@login_required
def cita_pdf(request, pk):
    """
    HU06-fix: Reporte PDF de una cita.
    Si WeasyPrint está instalado devuelve PDF descargable;
    si no, devuelve HTML con botón window.print().
    """
    cita = get_object_or_404(Cita, pk=pk)
    contexto = {
        "cita": cita,
        "mascota": cita.mascota,
        "dueno": cita.mascota.id_dueno,
        "veterinario": cita.veterinario,
        "tipo_servicio_display": cita.get_tipo_servicio_display(),
        "fecha_generacion": timezone.now(),
    }

    html_str = render_to_string("agendamiento/cita_pdf.html", contexto, request=request)

    try:
        from weasyprint import HTML as WP_HTML
        pdf_bytes = WP_HTML(string=html_str, base_url=request.build_absolute_uri("/")).write_pdf()
        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response["Content-Disposition"] = (
            f'attachment; filename="cita_{cita.pk}_{cita.mascota.nombre}.pdf"'
        )
        return response
    except ImportError:
        return HttpResponse(html_str)
