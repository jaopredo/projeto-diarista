from rest_framework import serializers
from web.models import Diaristas
from random import randint


class DiaristaCidadeSerializer(serializers.ModelSerializer):
    reputacao = serializers.SerializerMethodField()
    class Meta:
        model = Diaristas
        fields = ('nome_completo', 'foto', 'cidade', 'reputacao')
    
    def get_reputacao(self, obj):
        return randint(0, 5)
