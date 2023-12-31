from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=128)
    numero_colegiado = models.CharField(max_length=64)
    especialidad = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=128)
    dpi = models.CharField(max_length=64)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=128)
    numero_telefonico = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    diagnostico = models.CharField(max_length=128, blank=True, null=True)
    receta_medica = models.CharField(max_length=128, blank=True, null=True)
    razon_de_visita = models.CharField(max_length=128, blank=True, null=True)
    cita_hecha = models.BooleanField(default=False)

    def estado_cita(self):
        return 'Realizado' if self.cita_hecha else 'No Realizado'

    def __str__(self):
        return f"---Médico: {self.medico.nombre} - {self.fecha_cita} - Diagnóstico: {self.diagnostico} - Receta Médica: {self.receta_medica} - Razón de Visita: {self.razon_de_visita} - Entregado: {self.estado_cita()}"
