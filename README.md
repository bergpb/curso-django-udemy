### SimpleMOOC - Curso de Django da Udemy

O curso por padrão usa o Django 1.6 mas neste projeto utilizei a última versão do Django(2.2.5)

Requerimentos:
```python3```, ```pip``` e ```virtualenv```

Comandos iniciais:
1. mkdir simplemooc
2. virtualenv .venv
3. source .venv/bin/activate
4. pip install django
5. django-admin startproject simplemooc
6. django-admin startapp core

Rodando o projeto:
1. mkdir cursodjango
2. cd curso-django
3. git clone https://github.com/bergpb/curso-django-udemy.git
4. cd curso-django-udemy && virtualenv .env
5. pip install -r requirements.txt
6. python manage.py runserver
7. acesse a url: [localhost:8000](localhost:8000)