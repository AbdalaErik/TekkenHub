from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import *

# Create your views here.

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    
class PersonagemListView(ListView):

    model = Personagem
    context_object_name = "lista"
    template_name = "personagens/lista.html"

    def get_queryset(self):
        return Personagem.objects.all().order_by('id')

class PersonagemDetailView(DetailView):

    model = Personagem
    context_object_name = "detalhes"
    template_name = "personagens/detalhes.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    
class MecanicaView(View):

    def get(self, request, *args, **kwargs):
        mecanicas = Mecanica.objects.all()
        return render(request, 'mecanicas.html', {'mecanicas':mecanicas})

class TermoView(View):

    def get(self, request, *args, **kwargs):
        termos = Termo.objects.all().order_by("nome")
        return render(request, 'termos.html', {'termos':termos})
    
class MapaView(View):

    def get(self, request, *args, **kwargs):
        mapas = Mapa.objects.all()
        return render(request, 'mapas.html', {'mapas':mapas})
    
class PatchNoteView(View):

    def get(self, request, *args, **kwargs):
        patch_notes = PatchNote.objects.all().order_by("-id")
        return render(request, 'patch_notes.html', {'patch_notes':patch_notes})
    
class SobreView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'sobre.html')