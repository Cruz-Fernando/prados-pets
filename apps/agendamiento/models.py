from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, UniqueConstraint

from apps.directorio.models import Mascota


class Cita(models.Model):
    """
    HU: Como recepcionista, quiero agendar citas para consulta médica
    asignando fecha, hora y veterinario, para organizar la atención
    sin cruces de horario.

    NOTA: los nombres de campo (hora_inicio, hora_fin, tipo_servicio, etc.)
    y los db_column de mascota/veterinario están ajustados para coincidir
    con la tabla 'agendamiento_cita' ya existente en Supabase (creada por
    otro integrante del equipo). PENDIENTE: confirmar con el equipo si
    'id_usuario_creo_id' realmente representa al veterinario asignado o
    a quien creó el registro — de no ser así, falta agregar una columna
    real para el veterinario.
    """

    ESTADO_CHOICES = [
        ("programada", "Programada"),
        ("atendida", "Atendida"),
        ("cancelada", "Cancelada"),
    ]

    id_cita = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name="citas",
        db_column="id_mascota_id",
    )
    veterinario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="citas_asignadas",
        limit_choices_to={"id_rol__nombre_rol": "veterinario"},
        db_column="id_usuario_creo_id",
    )
    tipo_servicio = models.CharField(max_length=100, blank=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="programada")
    fecha_anterior = models.DateField(null=True, blank=True)
    hora_anterior = models.TimeField(null=True, blank=True)
    motivo_cancelacion = models.CharField(max_length=255, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ["fecha", "hora_inicio"]
        # RF24 — respaldo a nivel de base de datos: nunca puede haber dos
        # citas activas para el mismo veterinario en la misma fecha/hora.
        constraints = [
            UniqueConstraint(
                fields=["veterinario", "fecha", "hora_inicio"],
                condition=~Q(estado="cancelada"),
                name="unique_cita_veterinario_horario",
            )
        ]

    def __str__(self):
        return f"{self.mascota.nombre} - {self.fecha} {self.hora_inicio} ({self.veterinario})"

    def clean(self):
        # RF24 — validación también a nivel de modelo, por si se crea
        # una Cita fuera del formulario (admin, shell, otro flujo).
        if self.veterinario_id and self.fecha and self.hora_inicio:
            conflicto = Cita.objects.filter(
                veterinario_id=self.veterinario_id,
                fecha=self.fecha,
                hora_inicio=self.hora_inicio,
            ).exclude(estado="cancelada").exclude(pk=self.pk)

            if conflicto.exists():
                raise ValidationError(
                    "Este veterinario ya tiene una cita programada en esa fecha y hora."
                )