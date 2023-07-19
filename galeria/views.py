from django.shortcuts import render,get_object_or_404
from .models import Fotografia

def galeria (request):
    fotografia = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    dados = {
        'fotografia':fotografia
    }
    return render(request, 'galeria/index.html', dados)

def imagem (request, foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    dados = {
        'fotografia':fotografia
    }
    return render(request, 'galeria/imagem.html',dados)

def buscar (request):
    return render (request, 'galeria/buscar.html')