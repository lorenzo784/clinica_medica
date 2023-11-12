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

    path('historia', views.historia_view, name='historia'),
    path('contacto', views.contacto_view, name='contacto'),
    path('formularios', views.formulario_view, name='formulario'),

    path('crear_cita/<int:paciente_id>/', views.CitaCreateView.as_view(), name='cita-create'),
    path('cita/editar/<int:pk>/', views.CitaUpdateView.as_view(), name='cita-edit'),
    path('cita/', views.CitaListView.as_view(), name='cita-list'),
    path('cita/<int:pk>/', views.CitaDetailView.as_view(), name='cita-detail'),
    path('paciente/<int:pk>/citas/', views.CitasPacienteView.as_view(), name='citas-paciente'),
    path('cita/<int:pk>/delete/', views.CitaDeleteView.as_view(), name='cita-delete'),
]