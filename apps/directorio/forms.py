from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['id_dueno', 'nombre', 'especie', 'raza', 'tamano', 'sexo', 'fecha_nacimiento', 'condicion_pelaje']
        widgets = {
            'id_dueno': forms.Select(attrs={'class': 'w-full border rounded p-2'}),
            'nombre': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'especie': forms.Select(attrs={'class': 'w-full border rounded p-2'}),
            'raza': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'tamano': forms.Select(attrs={'class': 'w-full border rounded p-2'}),
            'sexo': forms.Select(attrs={'class': 'w-full border rounded p-2'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border rounded p-2'}),
            'condicion_pelaje': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
        }