from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarefa

def initial(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'index.html', {'tarefas': tarefas})

def cadastro(request):
    if request.method == 'POST':
        tarefa = Tarefa()
        tarefa.tarefa = request.POST['tarefa']
        tarefa.inicio = request.POST['inicio']
        tarefa.fim = request.POST['fim']
        tarefa.status = request.POST['status']
        tarefa.save()
        tarefas = Tarefa.objects.all()
        return render(request, 'index.html', {'tarefas': tarefas}) 
    else:
        return render(request, 'cadastro.html')