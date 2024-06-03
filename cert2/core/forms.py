from django import forms
from .models import Proyecto

class PropuestaProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'tema']