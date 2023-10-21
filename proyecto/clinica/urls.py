from django.urls import path
from . import views

app_name = 'clinica'

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/create', views.PacienteCreateView.as_view(), name='paciente-create'),
    path('paciente', views.PacienteListView.as_view(), name='paciente-list'),
    path('paciente/editar/<int:pk>', views.PacienteUpdateView.as_view(), name='paciente-update'),
    path('paciente/eliminar/<int:pk>', views.PacienteDeleteView.as_view(), name='paciente-delete'),

    path('medico/create', views.MedicoCreateView.as_view(), name='medico-create'),
    path('medico', views.MedicoListView.as_view(), name='medico-list'),
    path('medico/editar/<int:pk>', views.MedicoUpdateView.as_view(), name='medico-update'),
    path('medico/eliminar/<int:pk>', views.MedicoDeleteView.as_view(), name='medico-delete'),
]
