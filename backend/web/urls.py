from django.urls import path
from .views import cadastrar_diarista, listar_diaristas

urlpatterns = [
    path('cadastrar_diarista', cadastrar_diarista, name="cadastrar_diarista"),
    path('listar_diaristas', listar_diaristas, name="listar_diaristas"),
]