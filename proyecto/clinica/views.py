from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm
from django.urls import reverse_lazy


def home(request):
    return render(request, 'clinica/home.html')

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente-create')