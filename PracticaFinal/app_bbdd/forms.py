from django import forms
from .models import Actividad,UsuarioInscrito,Monitor,Sala,ResponsableSala

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioInscrito
        fields = '__all__'

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = ResponsableSala
        fields = '__all__'