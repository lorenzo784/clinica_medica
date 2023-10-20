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
            'razon_de_visita',
            'receta_medica',
            'numero_telefonico',
        ]

        labels = {
            'nombre': 'Nombre completo',
            'dpi': 'Número de DPI',
            'fecha_de_nacimiento': 'Fecha de nacimiento',
            'direccion': 'Dirección',
            'razon_de_visita': 'Razón de visita',
            'receta_medica': 'Receta médica',
            'numero_telefonico': 'Número telefónico'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'dpi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su numero de DPI'
                    }
                ),
            'fecha_de_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su numero de DPI'
                }
            ),
            'direccion': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'razon_de_visita': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'receta_medica': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'numero_telefonico': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }