from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'clinica/home.html')


class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/paciente/paciente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pacientes = Paciente.objects.all()
        citas_por_paciente = {}

        for paciente in pacientes:
            citas_no_hechas = Cita.objects.filter(paciente=paciente, cita_hecha=False)
            citas_por_paciente[paciente] = citas_no_hechas
        
        print(citas_por_paciente)

        context['citas_por_paciente'] = citas_por_paciente
        return context

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


class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita/cita_form.html'
    success_url = reverse_lazy('clinica:paciente-list')

    def form_valid(self, form):
        # Obtén el paciente que se pasa como parámetro en la URL
        paciente_id = self.kwargs['paciente_id']
        paciente = get_object_or_404(Paciente, pk=paciente_id)

        # Asigna el paciente al formulario antes de guardarlo
        form.instance.paciente = paciente

        # Llama al método form_valid de la clase base para continuar con el proceso de guardado
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'clinica/cita/cita_form.html'

    def get_success_url(self):
        paciente_id = self.object.paciente.id
        return reverse_lazy('clinica:citas-paciente', kwargs={'pk': paciente_id})

class CitaListView(ListView):
    model = Cita
    template_name = 'cita_list.html'

class CitaDetailView(DetailView):
    model = Cita
    template_name = 'cita_detail.html'

class CitasPacienteView(DetailView):
    model = Paciente
    template_name = 'clinica/cita/paciente/citas_paciente.html'
    context_object_name = 'paciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente = self.object
        citas_paciente = paciente.cita_set.all()
        context['paciente'] = paciente
        context['citas_paciente'] = citas_paciente
        return context

@method_decorator(login_required, name='dispatch')
class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'clinica/cita/paciente/cita_confirm_delete.html'
    success_url = reverse_lazy('clinica:paciente-list')