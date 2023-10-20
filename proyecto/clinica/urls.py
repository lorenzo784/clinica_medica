from django.urls import path
from . import views

app_name = 'clinica'

urlpatterns = [
    path('', views.home, name='home'),
    path('paciente/create', views.PacienteCreateView.as_view(), name='paciente-create')
]
