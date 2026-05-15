from django.shortcuts import get_object_or_404, redirect, render
from .forms import AlunoForm
from .models import Aluno


def aluno_list(request):
	alunos = Aluno.objects.all().order_by('nome')
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
