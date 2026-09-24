from django.urls import path

from . import views

app_name = "agendamiento"

urlpatterns = [
    path("agendar/", views.agendar_cita, name="agendar_cita"),
]