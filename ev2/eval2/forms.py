from django import forms
from eval2.models import Participante

class RegUser(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'