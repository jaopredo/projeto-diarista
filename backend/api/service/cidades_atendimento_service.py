from web.services import cep_service
from web.models import Diaristas
from rest_framework import serializers
import json


def listar_diaristas_cidade(cep):
    ibge = buscar_cidade_cep(cep)["ibge"]
    try:
        diaristas = Diaristas.objects.filter(codigo_ibge=ibge).order_by('id')
        return diaristas
    except Diaristas.DoesNotExist:
        return []


def buscar_cidade_cep(cep):
    response = cep_service.buscar_cidade_cep(cep)

    if response.status_code == 400:
        raise serializers.ValidationError("O CEP INFORMADO ESTÁ INCORRETO")  
    cidade_api = json.loads(response.content)
    if 'erro' in cidade_api: 
        raise serializers.ValidationError("O CEP INFORMADO NÃO EXISTE")
    
    return cidade_api
