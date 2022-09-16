from django import forms
from ..models import Diaristas


class DiaristaForm(forms.ModelForm):
    class Meta:
        model = Diaristas
        fields = '__all__'
