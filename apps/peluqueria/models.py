from django.db import models

class CitaPeluqueria(models.Model):
    TAMANO_CHOICES = [
        ('PEQUENO', 'Pequeño (1 - 10 kg)'),
        ('MEDIANO', 'Mediano (11 - 25 kg)'),
        ('GRANDE', 'Grande (Más de 25 kg)'),
    ]

    SERVICIO_CHOICES = [
        ('CORTE', 'Corte de pelo y peinado'),
        ('BANO', 'Baño e higiene básica'),
        ('COMPLETO', 'Baño, Corte y Spa completo'),
    ]

    nombre_mascota = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES, default='MEDIANO')
    servicio = models.CharField(max_length=20, choices=SERVICIO_CHOICES, default='BANO')
    fecha_hora = models.DateTimeField()
    duracion_estimada_min = models.IntegerField(default=60) # RF25
    observaciones = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita Peluquería: {self.nombre_mascota} - {self.get_servicio_display()}"