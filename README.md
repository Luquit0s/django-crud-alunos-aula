# CRUD de Alunos com Django

Projeto didático para demonstrar um CRUD básico com Django.

## Requisitos

- Python 3.12+
- pip

## Como executar

1. Criar ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Aplicar migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Executar servidor:

```bash
python manage.py runserver
```

5. Acessar no navegador:

- App CRUD: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Funcionalidades CRUD

- Criar aluno
- Listar alunos
- Editar aluno
- Excluir aluno

## Estrutura principal

- `escola/` configuracoes do projeto
- `alunos/models.py` modelo `Aluno`
- `alunos/forms.py` formulario com `ModelForm`
- `alunos/views.py` views de CRUD
- `alunos/urls.py` rotas do app
- `alunos/templates/alunos/` templates HTML

## Sugestao de atividades para alunos

1. Adicionar campo `curso` no modelo.
2. Criar filtro por nome na listagem.
3. Adicionar pagina de detalhes do aluno.
4. Melhorar o layout com Bootstrap.
