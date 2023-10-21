from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm
from django.urls import reverse_lazy


def home(request):
    return render(request, 'clinica/home.html')


class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/paciente/paciente_list.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente-list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente-list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'clinica/paciente/paciente_delete.html'
    success_url = reverse_lazy('clinica:paciente-list')