from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'idade', 'criado_em')
	search_fields = ('nome', 'email')
