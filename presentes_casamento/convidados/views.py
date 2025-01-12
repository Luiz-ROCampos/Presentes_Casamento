from django.shortcuts import redirect, render
from django.urls import reverse
from noivos.models import Convidados, Presentes
from . models import Acompanhantes
from django.http import HttpResponse


def convidados(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        convidado = Convidados.objects.get(token=token)
        presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
        acompanhantes = Acompanhantes.objects.filter(acompanhante_de=convidado)
        return render(request, 'convidados.html', {'convidado': convidado, 'presentes': presentes, 'acompanhantes': acompanhantes})
    elif request.method == 'POST':
        nome_acompanhante = request.POST.get('nome')
        token = request.GET.get('token')
        convidado = Convidados.objects.get(token=token)
        
        #TODO: Realizar o preenchimento de acompanhantes
        quantidade_acompanhantes = Acompanhantes.objects.filter(acompanhante_de=convidado).count()

        if quantidade_acompanhantes < convidado.maximo_acompanhantes:
            acompanhantes = Acompanhantes(
                nome_acompanhante = nome_acompanhante,
                acompanhante_de = convidado
            )

            acompanhantes.save()
            return redirect(f'/convidados/?token={token}')
        else:
            return redirect(f'/convidados/?token={token}')
    

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)

    if resposta not in ['C', 'R']:
        return redirect(f'/convidados/?token={token}')
    
    convidado.status = resposta
    convidado.save()

    return redirect(f'/convidados/?token={token}')

def reservar_presente(request, id):
    token = request.GET.get('token')

    convidado = Convidados.objects.get(token=token)
    presente = Presentes.objects.get(id=id)

    presente.reservado=True
    presente.reservado_por = convidado
    presente.save()
    return redirect(f'{reverse('convidados')}?token={token}')

    
    

    