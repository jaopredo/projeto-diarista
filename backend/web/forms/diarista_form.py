import json
from django import forms
from ..models import Diaristas
from ..services.cep_service import buscar_cidade_cep


class DiaristaForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "000.000.000-00"}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "00000-000"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': "(00) 00000-0000"}))
    # codigo_ibge = forms.IntegerField(required=False)

    class Meta:
        model = Diaristas
        exclude = ('codigo_ibge', )
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        return cpf.replace(".", "").replace("-", "")

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        cep_formatado = cep.replace("-", "")

        response = buscar_cidade_cep(cep_formatado)
        if response.status_code == 400:
            raise forms.ValidationError("O CEP INFORMADO ESTÁ INCORRETO")  
        cidade_api = json.loads(response.content)
        if 'erro' in cidade_api:
            raise forms.ValidationError("O CEP INFORMADO NÃO EXISTE")

        return cep.replace("-", "")
    
    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        return telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

    def save(self, commit=True):
        instance = super(DiaristaForm, self).save(commit=False)
        response = buscar_cidade_cep(self.cleaned_data.get('cep'))
        cidade_api = json.loads(response.content)
        instance.codigo_ibge = cidade_api['ibge']
        instance.save()
        return instance
