from django.shortcuts import render
from django.http import HttpResponse, Http404
from app.models import usuario, post

def index(request, arroba):
    try: 
        arroba = usuario.objects.get(pk=arroba)
    except arroba.DoesNotExist:
        raise Http404('Arroba não encontrado') #n funfa
    try:
        publi = post.objects.filter(arroba=arroba)
    except publi.DoesNotExist:
        raise Http404('Publicação não encontrada')#n funfa
    return render(request, 'app/index.html', {'publi' : publi, 'arroba': arroba})