from django.db import models


class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField(blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    es_recurrente = models.BooleanField(default=False)
    numero_visitas = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"

    def __str__(self):
        return self.nombre_completo


class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ("perro", "Perro"),
        ("gato", "Gato"),
        ("otro", "Otro"),
    ]

    id_mascota = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name="mascotas")
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100, blank=True)
    tamano = models.CharField(max_length=20, blank=True)
    sexo = models.CharField(max_length=10, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    condicion_pelaje = models.CharField(max_length=100, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return f"{self.nombre} ({self.id_dueno.nombre_completo})"
