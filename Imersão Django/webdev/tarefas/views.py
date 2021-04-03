from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tarefas.forms import TarefaNovaForm

def home(request):
    if request.method == 'POST': # Caso os dados do formulário serem válidos.
        form = TarefaNovaForm(request.POST)
        if form.is_valid(): # São válidos?
            form.save() # Salva no banco de dados.
            return HttpResponseRedirect(reverse('tarefas:home')) # Redireciona para home de tarefas.
        else: # Não são válidos?
            return (render(request, 'tarefas/home.html', {'form': form}, status=400))
    return render(request, ('tarefas/home.html'))