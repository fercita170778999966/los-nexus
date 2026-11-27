from django import forms
from .models import Usuario, Incidencia, Sugerencia, Servicio


class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['first_name', 'email', 'password']
        labels = {
            'first_name': 'Nombre completo',
            'email': 'Correo institucional',
        }


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['titulo', 'servicio', 'problema_relacionado', 'descripcion', 'ubicacion']
        labels = {
            'titulo': 'Problema',
            'servicio': 'Servicio',
            'problema_relacionado': 'Problema Relacionado',
            'descripcion': 'Descripción del problema',
            'ubicacion': 'Ubicación',
        }


class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ['titulo', 'desarrollo']
        labels = {
            'titulo': 'Título de la propuesta',
            'desarrollo': 'Propuesta / Desarrollo',
        }


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name']
        labels = {'first_name': 'Nombre del titular'}

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'responsable_nombre', 'responsable_correo']
