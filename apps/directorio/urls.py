from django.urls import path
from . import views

urlpatterns = [
    path('registrar-dueno/', views.registrar_dueno, name='registrar_dueno'),
]