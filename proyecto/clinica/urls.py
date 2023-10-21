from django.urls import path
from . import views

app_name = 'clinica'

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/create', views.PacienteCreateView.as_view(), name='paciente-create'),
    path('paciente', views.PacienteListView.as_view(), name='paciente-list'),
    path('paciente/editar/<int:pk>', views.PacienteUpdateView.as_view(), name='paciente-update'),
    path('paciente/eliminar/<int:pk>', views.PacienteDeleteView.as_view(), name='paciente-delete'),
]
