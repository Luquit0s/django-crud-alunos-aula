from django.test import TestCase
from django.urls import reverse
from .models import Aluno


class AlunoModelTest(TestCase):
	def test_str_retorna_nome(self):
		aluno = Aluno.objects.create(nome='Maria', email='maria@example.com', idade=20)
		self.assertEqual(str(aluno), 'Maria')


class AlunoViewsTest(TestCase):
	def test_aluno_list_status_code(self):
		response = self.client.get(reverse('aluno_list'))
		self.assertEqual(response.status_code, 200)
