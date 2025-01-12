from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Presentes, Convidados

# Create your views here.
def home(request):
    if request.method == 'GET':
        presentes = Presentes.objects.all()
        nao_reservado = Presentes.objects.filter(reservado=False).count()
        reservado = Presentes.objects.filter(reservado=True).count()
        data = [nao_reservado, reservado]
        return render(request, 'home.html', {'presentes': presentes, 'data': data})
    elif request.method == 'POST':
        nome_presente = request.POST.get('nome_presente')
        preco = request.POST.get('preco')
        importancia = int(request.POST.get('importancia'))
        foto = request.FILES.get('foto')
        
        if importancia < 1 or importancia > 5:
            return redirect('home')
        
        novo_presente = Presentes(
            nome_presente = nome_presente,
            preco = preco,
            importancia = importancia,
            foto = foto
        )

        novo_presente.save()
        
        return redirect('home')
    

def lista_convidados(request):
    if request.method == 'GET':
        convidados = Convidados.objects.all()
        return render(request, 'lista_convidados.html', {'convidados': convidados})
    elif request.method == 'POST':
        nome_convidado = request.POST.get('nome_convidado')
        whatsapp = request.POST.get('whatsapp')
        maximo_acompanhantes = int(request.POST.get('maximo_acompanhantes'))

        convidados = Convidados(
            nome_convidado=nome_convidado,
            whatsapp=whatsapp,
            maximo_acompanhantes=maximo_acompanhantes
        )

        convidados.save()

        return redirect('lista_convidados')
    
   