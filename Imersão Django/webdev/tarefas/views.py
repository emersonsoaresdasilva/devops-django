from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from webdev.tarefas.forms import TarefaNovaForm
from webdev.tarefas.models import Tarefa

def home(request):
    if request.method == 'POST': # Caso os dados do formulário serem válidos.
        form = TarefaNovaForm(request.POST)
        if form.is_valid(): # São válidos?
            form.save() # Salva no banco de dados.
            return HttpResponseRedirect(reverse('tarefas:home')) # Redireciona para home de tarefas.
        else: # Não são válidos?
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})