from django import forms
from .models import Paciente, Medico

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = [
            'nombre',
            'dpi',
            'fecha_de_nacimiento',
            'direccion',
            'numero_telefonico',
        ]

        labels = {
            'nombre': 'Nombre completo',
            'dpi': 'Número de DPI',
            'fecha_de_nacimiento': 'Fecha de nacimiento',
            'direccion': 'Dirección',
            'numero_telefonico': 'Número telefónico',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'dpi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de DPI'}),
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección residencial'}),
            'numero_telefonico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número telefónico'}),
        }


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico

        fields = [
            'nombre',
            'numero_colegiado',
            'especialidad',
        ]

        labels = {
            'nombre': 'Nombre completo',
            'numero_colegiado': 'Número de colegiado',
            'especialidad': 'Especialidad',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'numero_colegiado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número de colegiado'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su especialidad'}),
        }

from django import forms
from .models import Cita

from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita

        fields = [
            'medico',
            'razon_de_visita',
            'diagnostico',
            'receta_medica',
            'cita_hecha',
        ]

        labels = {
            'medico': 'Médico',
            'razon_de_visita': 'Razón de Visita',
            'diagnostico': 'Diagnóstico',
            'receta_medica': 'Receta Médica',
            'cita_hecha': 'Cita Finalizada',
        }

        widgets = {
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'razon_de_visita': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la razón de la visita'}),
            'diagnostico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el diagnóstico'}),
            'receta_medica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la receta médica'}),
            'cita_hecha': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'paciente': forms.HiddenInput(),
        }
