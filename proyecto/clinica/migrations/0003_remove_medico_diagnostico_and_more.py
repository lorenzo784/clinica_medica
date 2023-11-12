# Generated by Django 4.2.6 on 2023-11-12 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_paciente_medico_asociado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='medico_asociado',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='razon_de_visita',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='receta_medica',
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.CharField(max_length=128)),
                ('receta_medica', models.CharField(max_length=128)),
                ('razon_de_visita', models.CharField(max_length=128)),
                ('cita_hecha', models.BooleanField(default=False)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.paciente')),
            ],
        ),
    ]