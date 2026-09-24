from django import forms
from django.core.exceptions import ValidationError

from .models import Cita


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["mascota", "veterinario", "tipo_servicio", "fecha", "hora_inicio", "hora_fin"]
        widgets = {
            "mascota": forms.Select(attrs={"class": "form-control"}),
            "veterinario": forms.Select(attrs={"class": "form-control"}),
            "tipo_servicio": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: consulta general, vacunación…",
            }),
            "fecha": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "hora_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "hora_fin": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        }

    def clean(self):
        cleaned = super().clean()
        veterinario = cleaned.get("veterinario")
        fecha = cleaned.get("fecha")
        hora_inicio = cleaned.get("hora_inicio")
        if veterinario and fecha and hora_inicio:
            conflicto = Cita.objects.filter(
                veterinario=veterinario, fecha=fecha, hora_inicio=hora_inicio,
            ).exclude(estado="cancelada")

            if self.instance.pk:
                conflicto = conflicto.exclude(pk=self.instance.pk)

            if conflicto.exists():
                raise ValidationError(
                    f"El veterinario {veterinario} ya tiene una cita agendada "
                    f"el {fecha} a las {hora_inicio}. Elige otra hora u otro veterinario."
                )
        return cleaned