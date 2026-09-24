from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect, render

from .forms import CitaForm


@login_required
def agendar_cita(request):
    """
    HU: Como recepcionista, quiero agendar citas para consulta médica
    asignando fecha, hora y veterinario, para organizar la atención
    sin cruces de horario.
    """
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