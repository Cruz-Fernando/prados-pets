from django.urls import path
from . import views

app_name = 'peluqueria'

urlpatterns = [
    path('agendar/', views.agendar_peluqueria, name='agendar'),
]