from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente, Medico
from .forms import PacienteForm, MedicoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


def home(request):
    return render(request, 'clinica/home.html')


class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/paciente/paciente_list.html'

@method_decorator(login_required, name='dispatch')
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente/paciente_form.html'
    success_url = reverse_lazy('clinica:paciente-list')

@method_decorator(login_required, name='dispatch')
class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente/paciente_update.html'
    success_url = reverse_lazy('clinica:paciente-list')

@method_decorator(login_required, name='dispatch')
class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'clinica/paciente/paciente_delete.html'
    success_url = reverse_lazy('clinica:paciente-list')

class MedicoListView(ListView):
    model = Medico
    template_name = 'clinica/medico/medico_list.html'

@method_decorator(login_required, name='dispatch')
class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico/medico_form.html'
    success_url = reverse_lazy('clinica:medico-list')

@method_decorator(login_required, name='dispatch')
class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'clinica/medico/medico_update.html'
    success_url = reverse_lazy('clinica:medico-list')

@method_decorator(login_required, name='dispatch')
class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'clinica/medico/medico_delete.html'
    success_url = reverse_lazy('clinica:medico-list')

def historia_view(request):
    return render(request, 'clinica/web/historia.html')

def contacto_view(request):
    return render(request, 'clinica/web/contacto.html')

def formulario_view(request):
    return render(request, 'clinica/web/formulario.html')