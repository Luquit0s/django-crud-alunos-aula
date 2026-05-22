from django.shortcuts import get_object_or_404, redirect, render
from .forms import AlunoForm
from .models import Aluno


def aluno_list(request):
    nome_busca = request.GET.get('search')  # Captura o texto que o usuário digitou
    alunos = Aluno.objects.all().order_by('nome')
    
    if nome_busca:
        # Filtra os alunos cujo nome contenha o texto digitado (ignora maiúsculas/minúsculas)
        alunos = alunos.filter(nome__icontains=nome_busca)
        
    return render(request, 'alunos/aluno_list.html', {'alunos': alunos})

def aluno_create(request):
	form = AlunoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('aluno_list')

	return render(
		request,
		'alunos/aluno_form.html',
		{'form': form, 'titulo': 'Cadastrar aluno'},
	)


def aluno_update(request, pk):
	aluno = get_object_or_404(Aluno, pk=pk)
	form = AlunoForm(request.POST or None, instance=aluno)
	if form.is_valid():
		form.save()
		return redirect('aluno_list')

	return render(
		request,
		'alunos/aluno_form.html',
		{'form': form, 'titulo': 'Editar aluno'},
	)


def aluno_delete(request, pk):
	aluno = get_object_or_404(Aluno, pk=pk)
	if request.method == 'POST':
		aluno.delete()
		return redirect('aluno_list')

	return render(request, 'alunos/aluno_confirm_delete.html', {'aluno': aluno})


def aluno_detail(request, pk):
    # Busca o aluno pelo ID (pk). Se não achar, joga um erro 404 (Página não encontrada)
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'alunos/aluno_detail.html', {'aluno': aluno})