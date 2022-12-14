from django.shortcuts import redirect, render
from .forms import diarista_form
from .models import Diaristas

# Create your views here.
def cadastrar_diarista(request):
    if request.method == "POST":
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})


def listar_diaristas(request):
    diaristas = Diaristas.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})


def editar_diarista(request, id):
    diarista = Diaristas.objects.get(id=id)
    # Formulário com os dados preenchidos
    form_diarista = diarista_form.DiaristaForm(request.POST or None, instance=diarista)
    if form_diarista.is_valid():
        form_diarista.save()
        return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm(instance=diarista)
    return render(request, 'form_diarista.html', { 'form_diarista': form_diarista })

def remover_diarista(request, diarista_id):
    diarista = Diaristas.objects.get(id=diarista_id)
    diarista.delete()
    return redirect('listar_diaristas')